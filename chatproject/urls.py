from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from chat import views as chat_views
from django.shortcuts import render

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),

    # AUTH
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', chat_views.signup_view, name='signup'),

    # LANDING PAGE
    path("", lambda request: render(request, "home.html"), name="home"),

    # CHAT APP ROUTES
    path("", include("chat.urls")),
]
