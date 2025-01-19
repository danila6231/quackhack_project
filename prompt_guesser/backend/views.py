from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import base64
from django.shortcuts import get_object_or_404
from .models import Session
from .serializers import SessionSerializer, CreateSessionSerializer, JoinSessionSerializer, ProcessPromptSerializer, ProcessPromptGuessesSerializer
import requests
import os
from django.http import JsonResponse


class CreateSessionView(APIView):
    def post(self, request):
        serializer = CreateSessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        player_name = serializer.validated_data.get('player_name')

        session = Session.objects.create(player_one_name=player_name)
        response_serializer = SessionSerializer(session)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)
    
class GetSessionView(APIView):
    def get(self, request, session_name):
        session = get_object_or_404(Session, session_name=session_name)
        response_serializer = SessionSerializer(session)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

class JoinSessionView(APIView):
    def post(self, request, session_name):
        serializer = JoinSessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        player_name = serializer.validated_data['player_name']

        session = get_object_or_404(Session, session_name=session_name)
        if session.is_full():
            return Response({'error': 'Session is already full'}, status=status.HTTP_400_BAD_REQUEST)
        
        if session.player_one_name is None:
            session.player_one_name = player_name
        elif session.player_two_name is None:
            session.player_two_name = player_name
        
        session.save()
        response_serializer = SessionSerializer(session)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

class DeleteSessionView(APIView):
    def delete(self, request, session_name):
        session = get_object_or_404(Session, session_name=session_name)
        session.delete()
        return Response({'message': f'Session {session_name} deleted successfully'}, status=status.HTTP_200_OK)

class ListSessionsView(APIView):
    def get(self, request):
        sessions = Session.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ProcessPrompt(APIView):
    def post(self, request, session_name):
        serializer = ProcessPromptSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        

        # Extract the `prompt` field from the validated data
        prompt = serializer.validated_data.get('prompt')
        
        # Retrieve the session object
        session = get_object_or_404(Session, session_name=session_name)

        # Update the session with the new prompt
        session.prompt = prompt
        session.save()

        # Define the image URL
        image_url = "https://images.deepai.org/art-image/021223307047423898f5426c6d679a00/messi-and-ronaldo-playing-baseball-051fc3.jpg"

        try:
        # Fetch the image from the URL
            response = requests.get(image_url)
            if response.status_code != 200:
                return JsonResponse({'error': 'Failed to fetch the image'}, status=500)

            # Encode the image to Base64
            encoded_image = base64.b64encode(response.content).decode('utf-8')

            # Return the Base64 image in a JSON response
            return JsonResponse({
                'prompt': prompt,
                'encoded_image': encoded_image
            })

        except Exception as e:
            return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)
        
class ProcessPromptGuesses(APIView):
    def post(self, request, session_name):
        serializer = ProcessPromptGuessesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        

        # Extract the `prompt` field from the validated data
        prompt_guess = serializer.validated_data.get('prompt')
        
        # Retrieve the session object
        session = get_object_or_404(Session, session_name=session_name)

        # Update the session with the new prompt
        prompt = session.prompt

        session.prompt_guess = prompt_guess

        points = 0
        for word in prompt_guess.split():
            if word in prompt:
                points += 1
        
        session.player_two_score += points
        
        session.save()

        response_serializer = SessionSerializer(session)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
        
