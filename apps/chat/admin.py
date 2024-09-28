from django.contrib import admin
from django.contrib.admin import TabularInline

from apps.chat.models import Room, Message


class MessageInline(TabularInline):
    model = Message
    extra = 1


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    inlines = [MessageInline]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
