from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('', myapp.views.main, name="main"),
    path('profile/', myapp.views.profile, name="profile"),
]