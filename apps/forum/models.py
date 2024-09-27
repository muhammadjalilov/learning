from django.db import models

from apps.account.models import Account
from apps.courses.models import Course
from apps.shared.models import TimeStampedModel


class Post(TimeStampedModel):
    question = models.TextField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE,related_name='posts')
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.question


class Answer(TimeStampedModel):
    body = models.TextField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE,related_name='answers')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='answers')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.body
