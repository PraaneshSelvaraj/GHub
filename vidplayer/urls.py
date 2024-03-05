from django.urls import path
from .views import video_player

urlpatterns =[
    path("video/", video_player, name="video player"),    
]