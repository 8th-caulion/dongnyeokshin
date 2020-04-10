from django.contrib import admin
from django.urls import path
import photofolio.views

urlpatterns = [
    path('photofolio/', photofolio.views.photofolio, name = "photofolio"),
]