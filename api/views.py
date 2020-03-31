from django.shortcuts import render
from django.http import HttpResponse
from .services import get_episodes
import json

# Create your views here.
def index(request):
    episodes = get_episodes()
    return render(request, 'api/index.html', {'results': episodes})
