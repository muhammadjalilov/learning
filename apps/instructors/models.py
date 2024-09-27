from django.db import models

from apps.account.models import Account


class Instructor(Account):
    courses = models.ManyToManyField('apps.Course', related_name='instructors')

    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'

    def __str__(self):
        return str(self.get_full_name())
