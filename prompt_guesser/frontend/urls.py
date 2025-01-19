from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('list', session_list, name='session_list'),  # Serve 'index.html' at the root URL
    path('create-session', create_session, name='create_session'),
    path('join-session', join_session, name='join_session')
]
