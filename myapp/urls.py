from django.contrib import admin
from django.urls import path
import myapp.views


urlpatterns = [
    path('', myapp.views.main, name="main"),
    path('profile/', myapp.views.profile, name="profile"),
    path('new/',myapp.views.new, name="new"),
    path('blog/<int:blog_id>', myapp.views.detail, name="detail"),
    path('blog/create', myapp.views.create, name="create"),
]