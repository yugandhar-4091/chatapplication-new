from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import ChatRoom, Message


def room_list(request):
    rooms = ChatRoom.objects.all().order_by("name")
    return render(request, "chat/room_list.html", {"rooms": rooms})


@login_required
def room_view(request, room_name):
    room = get_object_or_404(ChatRoom, name=room_name)
    rooms = ChatRoom.objects.all().order_by("name")

    # Save text messages using POST method
    if request.method == "POST":
        text = request.POST.get("message", "").strip()

        if text:
            Message.objects.create(
                user=request.user,
                room=room,
                text=text,
                msg_type="text",
                status="sent"
            )

        return redirect("room", room_name=room.name)

    messages = Message.objects.filter(room=room).order_by("created_at")

    return render(request, "chat/room.html", {
        "room": room,
        "rooms": rooms,
        "messages": messages,
    })


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("room_list")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})
