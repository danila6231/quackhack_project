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
    
class PlayerStatusView(APIView):
    def get(self, request, session_name):
        session = get_object_or_404(Session, session_name=session_name)

        player_one_name = session.player_one_name
        player_two_name = session.player_two_name
        player_one_joined = player_one_name is not None
        player_two_joined = player_two_name is not None

        response = dict()
        response["player_one_joined"] = player_one_joined
        response["player_two_joined"] = player_two_joined

        if player_one_joined:
            response["player_one_name"] = player_one_name

        if player_two_joined:
            response["player_two_name"] = player_two_name


        return Response(
            response, status=status.HTTP_200_OK
        )
    

# class ImageStatusView(APIView):
#     def get(self, request, session_name):
#         session = get_object_or_404(Session, session_name=session_name)

#         if session.
    

class GuessStatusView(APIView):
    def get(self, request, session_name):
        session = get_object_or_404(Session, session_name=session_name)

        guess_is_made = session.prompt_guess is not None
        
        return Response({"guess_is_made": guess_is_made}, status=status.HTTP_200_OK)
            



    

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
        

        # Define the image URL
        # r = requests.post(
        #     "https://api.deepai.org/api/text2img",
        #     data={
        #         'text': 'messi and ronaldo playing baseball',
        #     },
        #     headers={'api-key': os.environ['OPENAI_KEY']}
        # )
        # image_url = r.json()['share_url']
        
        
        image_url = "https://images.deepai.org/art-image/021223307047423898f5426c6d679a00/messi-and-ronaldo-playing-baseball-051fc3.jpg"
        session.image_url = image_url
        session.save()
        try:
        # Fetch the image from the URL
            response = requests.get(image_url)
            if response.status_code != 200:
                return JsonResponse({'error': 'Failed to fetch the image'}, status=500)

            # Encode the image to Base64
            # encoded_image = base64.b64encode(response.content).decode('utf-8')

            
            response_serializer = SessionSerializer(session)
            return Response(response_serializer.data, status=status.HTTP_200_OK)

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
    

class EndTurnView(APIView):
    def patch(self, request, session_name):
        session = get_object_or_404(Session, session_name=session_name)

        if session.prompt is None:
            return Response({"message": "prompt is empty. Turn is not over."}, status=status.HTTP_403_FORBIDDEN)

        if session.prompt_guess is None:
            return Response({"message": "prompt_guess is empty. Turn is not over."}, status=status.HTTP_403_FORBIDDEN)


        session.turn += 1
        session.prompt = None
        session.prompt_guess = None

        session.save()

        return Response(SessionSerializer(session).data, status=status.HTTP_200_OK)


        
        
