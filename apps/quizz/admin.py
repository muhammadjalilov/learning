from django.contrib import admin
from django.contrib.admin import StackedInline

from apps.quizz.models import Quiz, Question, Answer


class QuestionInline(StackedInline):
    model = Question
    extra = 1


class AnswerInline(StackedInline):
    model = Answer
    extra = 1


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question']
    inlines = [AnswerInline]


@admin.register(Answer)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['question', 'is_correct']
