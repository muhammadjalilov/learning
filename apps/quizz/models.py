from django.db import models

from apps.shared.models import SlugStampedModel


class Quiz(SlugStampedModel):
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.name

class Question(SlugStampedModel):
    # name = Question
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.name


class Choice(SlugStampedModel):
    name = None
    choice_1 = models.TextField(verbose_name="Choice 1")
    choice_2 = models.TextField(verbose_name="Choice 2")
    choice_3 = models.TextField(verbose_name="Choice 3")
    right_answer = models.SmallIntegerField(verbose_name="Right answer")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'

    def __str__(self):
        return str(self.id)
