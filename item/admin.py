from django.contrib import admin

# Register your models here.
from .models import Category, Item

#adicionando category no admin
admin.site.register(Category)
admin.site.register(Item)