from django.contrib import admin
from django.contrib.admin import TabularInline

from apps.courses.models import Course, Category, Chapter, Topic


class CourseInline(TabularInline):
    model = Course
    extra = 1


class ChapterInline(TabularInline):
    model = Chapter
    extra = 1


class TopicInline(TabularInline):
    model = Topic
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [CourseInline]


@admin.register(Course)
class Admin(admin.ModelAdmin):
    list_display = ['description', 'price']
    inlines = [ChapterInline]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    inlines = [TopicInline]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
