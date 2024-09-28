from django.contrib import admin
from django.contrib.admin import TabularInline

from apps.forum.models import Post, Answer


class AnswerInline(TabularInline):
    model = Answer
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['question', 'user', 'course']
    inlines = [AnswerInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['body', 'post', 'parent']
