from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @action(methods=["get"], detail=True, url_path='messages-list')
    def messages_list(self, *args, **kwargs):
        room = self.get_object()
        serializer = MessageSerializer(room.messages, many=True)
        return Response(data=serializer.data)

    @action(methods=["post"], detail=True, url_path='message-create')
    def messages_create(self, request, *args, **kwargs):
        room = self.get_object()
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user, room=room)
        return Response(data=serializer.data)
