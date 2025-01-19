from rest_framework import serializers
from .models import Session

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['session_name', 'player_one_name', 'player_two_name', 'player_one_score', 'player_two_score', 'turn', 'created_at', 'prompt', 'prompt_guess', 'image_url']

class CreateSessionSerializer(serializers.Serializer):
    player_name = serializers.CharField(max_length=50, required=True)

class JoinSessionSerializer(serializers.Serializer):
    player_name = serializers.CharField(max_length=50, required=True)

class ProcessPromptSerializer(serializers.Serializer):
    prompt = serializers.CharField(required=True)


class ProcessPromptGuessesSerializer(serializers.Serializer):
    prompt = serializers.CharField(required=True)    