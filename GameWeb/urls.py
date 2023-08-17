from django.urls import path
from GameWeb import views

urlpatterns = [
   path('', views.games , name = "game-view"),
   path('game/', views.games_text , name = "game-text")
]