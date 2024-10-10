from django.contrib import admin
from django.contrib.admin import TabularInline

from apps.forum.models import ForumPost, Answer


class AnswerInline(TabularInline):
    model = Answer
    extra = 1


@admin.register(ForumPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ['question', 'user']
    inlines = [AnswerInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['body', 'post', 'parent']
