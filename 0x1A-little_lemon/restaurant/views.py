#!/usr/bin/python3
"""module to implement the views functions
"""

from django.shortcuts import render
from .forms import BookingForm
from .models import Menu


def home(request):
    """function that renders the home page of the web application
    
    Args:
        request: a HttpRequest
    """
    return render(request, "index.html")

def about(request):
    """function that renders the about page of the web application
    
    Args:
        request: a HttpRequest
    """
    return render(request, "about.html")

def book(request):
    """function that renders the reservaion page of the web app
    
    Args:
        request: a HttpRequest
    """
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid:
            form.save()
    context = {
        "form": form
        }
    return render(request, "book.html", context)

def menu(request):
    """function to render the menu items
    
    Args:
        request: a HttpRequest
    """
    menu_data = Menu.objects.all()
    main_data = {
        "menu": menu_data
    }
    return render(request, "menu.html", main_data)

def menu_items(request, pk=None):
    """function to render menu items based on the primary key value
    
    Args:
        pk (int): the primary key of the menu item
        request (httprequest): a HttpRequest
    """
    if pk is not None:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, "menu_items.html", {"menu_item": menu_item})