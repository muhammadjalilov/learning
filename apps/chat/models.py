from django.db import models

from apps.account.models import Account
from apps.shared.models import TimeStampedModel, SlugStampedModel


class Room(SlugStampedModel):
    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return self.name


class Message(TimeStampedModel):
    body = models.TextField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='messages')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='messages')

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.body
