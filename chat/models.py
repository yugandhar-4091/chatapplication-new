from django.db import models
from django.contrib.auth.models import User


# -------- ChatRoom Model --------
class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


# -------- Message Model --------
class Message(models.Model):

    STATUS_CHOICES = [
        ("sent", "Sent"),
        ("delivered", "Delivered"),
        ("seen", "Seen"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name="messages")
    
    text = models.TextField(blank=True, null=True)

    file = models.FileField(upload_to="uploads/", blank=True, null=True)

    msg_type = models.CharField(
        max_length=10,
        choices=[("text", "Text"), ("image", "Image"), ("file", "File")],
        default="text"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="sent")

    def __str__(self):
        return f"{self.user.username}: {self.text[:20] if self.text else '[file]'}"
