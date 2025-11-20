from django.contrib import admin
from .models import ChatRoom, Message


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "room", "msg_type", "created_at", "status")
    list_filter = ("msg_type", "status", "created_at")
    search_fields = ("text", "user__username", "room__name")
    ordering = ("-created_at",)
