from django.urls import path
from .views import *

urlpatterns = [
    path('', game_home, name='game_home'),
    path('list', game_list, name='game_list'),  # Serve 'index.html' at the root URL
]
