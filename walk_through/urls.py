from django.urls import path

from . import views

urlpatterns = [
    path('', views.walk_through, name='walk_through'),
]