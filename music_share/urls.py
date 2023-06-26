from django.contrib import admin
from django.urls import path
from music_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", views.register, name="register"),
    path("accounts/login/", views.user_login, name="login"),
]
