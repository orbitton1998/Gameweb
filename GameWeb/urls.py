from django.urls import path
from GameWeb import views

urlpatterns = [
   path('', views.games , name = "game-view"),
   path('login/', views.signin , name = "login"),
   path('logout/', views.logout_user , name = "logout"),
   path('register/', views.register, name='register'),
   path('home/', views.home , name = "home"),
   path('game/', views.games, name = "game-text"),
   path('place_order/<int:game_id>/', views.place_order, name='place-order'),
   path('add_game/', views.add_game, name='add-game'),
   path('update-game/<int:game_id>/', views.update_game, name='update-game'),
   path('delete-game/<int:game_id>/', views.delete_game, name='delete-game')
]