from django.urls import path
from . import views

urlpatterns = [
    path('metro_pos', views.get_metro_position, name='metro_positions'),
    path('', views.home, name='home'),  # Add this line for the home page
]