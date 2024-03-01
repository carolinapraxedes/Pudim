from django.shortcuts import render
from.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')