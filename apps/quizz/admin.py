from django.contrib import admin
from django.contrib.admin import StackedInline

from apps.quizz.models import Quiz, Question, Choice


class QuestionInline(StackedInline):
    model = Question
    extra = 1


class ChoiceInline(StackedInline):
    model = Choice
    extra = 1


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [QuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question']
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['right_answer']
