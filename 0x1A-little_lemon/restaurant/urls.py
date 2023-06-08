from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('about/', views.about, name = "about"),
    path('book/', views.book, name = "book"),
    path('menu/', views.menu, name='menu'),
    path('menu_items/<pk>/', views.menu_items, name="menu_items"),
]