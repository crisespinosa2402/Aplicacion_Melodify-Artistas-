
from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),  # Lista de canciones
    path('song/<int:song_id>/', views.song_detail, name='song_detail'),  # Detalles de una canción
]
