from django.contrib import admin
from django.contrib.admin import TabularInline

from apps.account.models import Account
from apps.instructors.models import Instructor
from apps.students.models import Student


class InstructorInline(TabularInline):
    model = Instructor
    extra = 1


class StudentInline(TabularInline):
    model = Student
    extra = 1


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    inlines = [InstructorInline, StudentInline]
