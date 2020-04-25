from django.contrib import admin
from django.urls import path
import myapp.views


urlpatterns = [
    path('', myapp.views.main, name="main"),
    path('profile/', myapp.views.profile, name="profile"),
    path('new/',myapp.views.new, name="new"),
    path('blog/<int:blog_id>', myapp.views.detail, name="detail"),
    path('blog/create', myapp.views.create, name="create"),
    path('blog/edit/<int:blog_id>', myapp.views.edit, name="edit"),
    path('blog/update/<int:blog_id>', myapp.views.update, name="update"),
    path('blog/delete/<int:blog_id>', myapp.views.delete, name="delete"),

]