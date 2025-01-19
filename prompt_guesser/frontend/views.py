from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def session_list(request):
    return render(request, 'all_sessions.html')

def create_session(request):
    return render(request, 'create_session.html')

def join_session(request):
    return render(request, 'join_session.html')