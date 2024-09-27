from django.db import models

from apps.account.models import Account
from apps.shared.models import TimeStampedModel


class Instructor(TimeStampedModel):
    account = models.OneToOneField('account.Account',on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'

    def __str__(self):
        return str(self.get_full_name())
