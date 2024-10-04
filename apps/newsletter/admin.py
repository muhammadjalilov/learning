from django.contrib import admin

from apps.newsletter.models import NewsletterEmails


@admin.register(NewsletterEmails)
class NewsletterEmailsAdmin(admin.ModelAdmin):
    list_display = ['email', 'remote_address']
