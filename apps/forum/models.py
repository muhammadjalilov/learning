from django.db import models

from apps.account.models import Account
from apps.courses.models import Course
from apps.shared.models import TimeStampedModel, SlugStampedModel


class ForumCategory(SlugStampedModel):
    is_verified = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Forum Category'
        verbose_name_plural = 'Forum Categories'

    def __str__(self):
        return self.name


class ForumPost(TimeStampedModel):
    question = models.TextField()
    category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.question


class Answer(TimeStampedModel):
    body = models.TextField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE,related_name='answers')
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE,related_name='answers')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.body
