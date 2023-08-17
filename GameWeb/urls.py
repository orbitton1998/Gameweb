from django.urls import path
from GameWeb import views

urlpatterns = [
   path('', views.games , name = "game-view"),
   path('login/', views.signin , name = "login"),
   path('logout/', views.logout_user , name = "logout"),
   path('game/', views.games_text , name = "game-text")
]