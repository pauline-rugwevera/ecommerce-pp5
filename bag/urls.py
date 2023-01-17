from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('', views.view_bag, name='view_bag'),
   path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
   path('adjust/<item_id>/', views.adjust_basket, name='adjust_bag'),
   path('remove/<item_id>/', views.remove_from_basket,
        name='remove_from_basket'),
]
