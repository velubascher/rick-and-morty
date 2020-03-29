from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def index(request):
    response = requests.get('https://rickandmortyapi.com/api/episode/')
    episodes_data = response.json()
    print(type(episodes_data))
    return render(request, 'api/index.html', episodes_data)
