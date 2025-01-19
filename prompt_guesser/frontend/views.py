from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def game_home(request):
    return render(request, 'dist/index.html')

def game_list(request):
    return render(request, 'all_sessions.html')