from django.urls import path
from .views import game_home

urlpatterns = [
    path('', game_home, name='game_home'),  # Serve 'index.html' at the root URL
]
