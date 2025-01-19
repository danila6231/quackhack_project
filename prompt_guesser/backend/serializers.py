from rest_framework import serializers
from .models import Session

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['session_name', 'player_one_name', 'player_two_name', 'created_at']

class CreateSessionSerializer(serializers.Serializer):
    player_name = serializers.CharField(max_length=50, required=False)

class JoinSessionSerializer(serializers.Serializer):
    player_name = serializers.CharField(max_length=50, required=True)
