from django.db import models

from apps.account.models import Account
from apps.instructors.models import Instructor
from apps.shared.models import SlugStampedModel, TimeStampedModel


class Quiz(SlugStampedModel):
    description = models.TextField(default=None)
    creator = models.ForeignKey(Instructor, on_delete=models.CASCADE, default=1)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)

    @property
    def num_questions(self):
        return self.questions.count()

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.name


class Question(TimeStampedModel):
    question = models.CharField(max_length=1000)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.question


class Answer(TimeStampedModel):
    choice = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    class Meta:
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'

    def __str__(self):
        return f"{str(self.choice)} (Correct: {self.is_correct})"


class QuizAttempt(TimeStampedModel):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='quiz_attempts')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='attempts')
    score = models.IntegerField(default=0)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Quiz Attempt'
        verbose_name_plural = 'Quiz Attempts'
        ordering = ('created_at',)

    def __str__(self):
        return f"{self.user.username} - {self.quiz} - Score: {self.score}"


class UserAnswer(TimeStampedModel):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='user_answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='user_answers')
    selected_answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='user_answers')

    class Meta:
        verbose_name = 'User Answer'
        verbose_name_plural = 'User Answers'

    def __str__(self):
        return f"Attempt by {self.attempt.user.username} on {self.question.question}: {self.selected_answer.question}"
