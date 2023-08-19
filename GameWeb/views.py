from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from GameWeb.models import Game, Customer
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm,OrderForm,GameForm
from django.contrib.auth.decorators import login_required,user_passes_test
from .models import Game, Order



def home(request):
     return render(request, 'home.html')

def is_superuser(user):
    return user.is_superuser

@login_required
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
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('game-view')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

from django.db import transaction

@login_required
def place_order(request, game_id):
    game = Game.objects.get(pk=game_id)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            if quantity <= 0:
                return render(request, 'place_order.html', {'game': game, 'form': form, 'error_message': 'Invalid quantity.'})
            
            if game.quantity >= quantity:
                with transaction.atomic():
                    order = Order.objects.create(
                        customer=request.user,  # Use request.user directly
                        game_details=game.name,
                    )
                    game.quantity -= quantity
                    game.save()
                    return render(request, 'order_success.html')  # Assuming you have an 'order_success.html' template
            else:
                return render(request, 'place_order.html', {'game': game, 'form': form, 'error_message': 'Insufficient stock.'})
    else:
        form = OrderForm(initial={'game_id': game_id})

    context = {'game': game, 'form': form}
    return render(request, 'place_order.html', context)

@login_required
@user_passes_test(is_superuser)
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)  # Make sure to handle file uploads
        if form.is_valid():
            form.save()
            return redirect('game-view')  # Redirect to the game view after adding the game
    else:
        form = GameForm()

    context = {'form': form}
    return render(request, 'add_game.html', context)

@login_required
@user_passes_test(is_superuser)
def delete_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    
    if request.method == 'POST':
        game.delete()
        return redirect('game-view')  # Redirect to the game view after deletion

    context = {'game': game}
    return render(request, 'delete_game.html', context)

@login_required
@user_passes_test(is_superuser)
def update_game(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    if request.method == 'POST':
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        
        try:
            price = float(price)
            quantity = int(quantity)
            
            if price >= 0 and quantity >= 0:
                game.price = price
                game.quantity = quantity
                game.save()
                return redirect('game-view')  # Redirect to the game view after updating
        except (ValueError, TypeError):
            pass
    
    context = {'game': game}
    return render(request, 'update_game.html', context)