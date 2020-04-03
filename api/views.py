from django.shortcuts import render
from django.http import HttpResponse
from .services import get_episodes, get_episode, get_character, get_location, make_search
import json

# Create your views here.
def index(request):
    episodes = get_episodes()
    return render(request, 'api/index.html', {'results': episodes})

def episode(request, episode_id):
    episodes = get_episode(episode_id)
    return render(request, 'api/episode.html', episodes)

def character(request, character_id):
    character = get_character(character_id)
    return render(request, 'api/character.html', character)

def location(request, location_id):
    location = get_location(location_id)
    return render(request, 'api/location.html', location)

def search(request, term):
    results = make_search(term)
    return render(request, 'api/search.html', results)

