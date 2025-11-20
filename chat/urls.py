from django.urls import path
from . import views

urlpatterns = [
    path("rooms/", views.room_list, name="room_list"),
    path("room/<str:room_name>/", views.room_view, name="room"),
]
