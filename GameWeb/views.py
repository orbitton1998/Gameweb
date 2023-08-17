from django.shortcuts import render, redirect
from django.http import HttpResponse
from GameWeb.models import Game, Customer
from django.contrib.auth import login, logout, authenticate
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


def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            customer=Customer.objects.get(username=username)
        except:
            return render(request, 'login.html', {'message': 'Username or Password incorrect'})
        customer=authenticate(request,username=username,password=password)
        if customer is None:
            return render(request, 'login.html', {'message': 'Username or Password incorrect'})
        else:
            login(request,customer)
            return redirect('game-view')


def logout_user(request):
    logout(request)
    return redirect('game-view')

