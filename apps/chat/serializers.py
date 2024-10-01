from rest_framework import serializers
from .models import Room, Message


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ['slug']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ['user', 'room']
