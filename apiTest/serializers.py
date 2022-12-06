from rest_framework import serializers

from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player1Hp', 'player2Hp']