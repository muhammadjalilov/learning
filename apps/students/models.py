from django.db import models

from apps.account.choices import AccountSubscriptions
from apps.account.models import Account
from apps.courses.models import Course
from apps.shared.models import SlugStampedModel, TimeStampedModel


class Student(TimeStampedModel):
    account = models.OneToOneField('account.Account',on_delete=models.CASCADE)
    subscription_type = models.CharField(max_length=128, choices=AccountSubscriptions,
                                         default=AccountSubscriptions.STARTER)
    courses = models.ManyToManyField(Course)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return str(self.account.get_full_name())


class Certificate(SlugStampedModel):
    file = models.FileField(upload_to='certificates')
    students = models.ManyToManyField(Student)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    def __str__(self):
        return str(self.name)


class Reward(SlugStampedModel):
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE, related_name='rewards')

    class Meta:
        verbose_name = 'Reward'
        verbose_name_plural = 'Rewards'

    def __str__(self):
        return str(self.name)
