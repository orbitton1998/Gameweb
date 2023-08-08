from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Customer(AbstractUser):
    age = models.IntegerField(null=True)
    adress = models.CharField(max_length=100 , null=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    order_deatails = models.CharField(max_length=1000 , null=False)


class Game(models.Model):
    
    name = models.CharField(max_length=100, null=False)
    janre = models.CharField(max_length=20 , null=False)    
    date_of_realese = models.IntegerField(null=False)
    image = models.ImageField(upload_to="game_images", default="/game_images/game.jpg")
    order = models.ForeignKey(Order , on_delete=models.CASCADE)




    

