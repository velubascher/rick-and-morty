from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('episodes/', views.index, name='index'),
    path('episode/<int:episode_id>/', views.episode, name='episode'),
]
