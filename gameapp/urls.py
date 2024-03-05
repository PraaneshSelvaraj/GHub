from django.urls import path
from .views import home_view,game_view

urlpatterns =[
    path("", home_view, name="home"),
    path("game/<str:name>", game_view, name="game")
]