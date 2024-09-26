from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.shared.models import BaseModel


class Account(AbstractUser, BaseModel):
    website = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to='avatars/')

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.username

