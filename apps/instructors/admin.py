from django.contrib import admin

from apps.instructors.models import Instructor


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    pass