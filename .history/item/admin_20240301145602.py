from django.contrib import admin

# Register your models here.
from .models import Category

#adicionando category no admin
admin.site.register(Category)