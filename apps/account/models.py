from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.shared.models import SlugStampedModel, TimeStampedModel


class Account(AbstractUser, TimeStampedModel):
    website = models.CharField(max_length=128)
    avatar = models.ImageField(upload_to='avatars/')
    is_subscribed_newsletter = models.BooleanField(default=False)
    card = models.ForeignKey('apps.CreditCard', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.username
