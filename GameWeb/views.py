from django.shortcuts import render , redirect
from django.http import HttpResponse
from GameWeb.models import Game
# Create your views here.

def games(request):
    all_games = Game.objects.all()
    context = {
        'games': all_games
    }
    return render(request, 'game.html', context)


def games_text(request):
    all_games = Game.objects.all()
    mystr = ""
    for games in all_games:
        mystr += str(games)
        mystr += "<br>"
    return HttpResponse(f"This is a list of games!<br>{mystr}")
   



