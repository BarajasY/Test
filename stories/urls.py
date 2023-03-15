from django.urls import path, include
from .models import Story
from . import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('allstories/', views.AllStories, name="stories"),
    path('<int:story_id>/', views.StoryById, name="stories")
]