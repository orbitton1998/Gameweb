from django.shortcuts import render
from django.http import HttpResponse
from GameWeb.models import Game
# Create your views here.

def GameWeb(request):
   return HttpResponse("Hello DJANGO Gaming Store")

def single_game(request ,game_id):
   game = game.objects.get(id = game.id)