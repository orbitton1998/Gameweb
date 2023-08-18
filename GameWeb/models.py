from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    phone_number = models.IntegerField(default=0)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    game_details = models.CharField(max_length=1000, null=False)  
    order_date = models.DateField(auto_now_add=True)

class Game(models.Model):
    name = models.CharField(max_length=100, null=False)
    genre = models.CharField(max_length=20, null=False)  
    price = models.IntegerField(null=False)
    image = models.ImageField(upload_to="game_images", default="/game_images/game.jpg")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} - {self.price} - {self.genre}"
