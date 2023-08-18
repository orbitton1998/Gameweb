# GameWeb/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Game

from GameWeb.models import Customer

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['username', 'password'] 

class OrderForm(forms.Form):
    game_id = forms.IntegerField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(min_value=1)

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'