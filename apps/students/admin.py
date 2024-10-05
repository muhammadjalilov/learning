from django.contrib import admin

from apps.students.models import Student, Certificate, Reward


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ("period",)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['file']

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ['certificate']

