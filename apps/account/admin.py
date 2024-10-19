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
    fieldsets = (
        (None, {
            "fields": ("first_name", "last_name", "username", "email", "password")
        }
         ),
        ("Permissions", {
            "fields": ("user_permissions", "groups", "is_superuser", "is_staff")
        }
         ),
        ("Important Date", {
            "fields": ("last_login",)
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'), }),)
    readonly_fields = ("last_login",)
