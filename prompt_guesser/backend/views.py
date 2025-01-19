from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Session
from .serializers import SessionSerializer, CreateSessionSerializer, JoinSessionSerializer

class CreateSessionView(APIView):
    def post(self, request):
        serializer = CreateSessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        player_name = serializer.validated_data.get('player_name')

        session = Session.objects.create(player_one_name=player_name)
        response_serializer = SessionSerializer(session)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

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
