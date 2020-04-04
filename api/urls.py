from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('episodes/', views.index, name='index'),
    path('episode/<int:episode_id>/', views.episode, name='episode'),
    path('character/<int:character_id>/', views.character, name='character'),
    path('location/<int:location_id>/', views.location, name='location'),
    path('search/', views.search, name='search'),
]
