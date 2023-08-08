from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Game , Customer , Order

admin.site.register(Customer , UserAdmin)
admin.site.register(Order)
admin.site.register(Game)
# Register your models here.
