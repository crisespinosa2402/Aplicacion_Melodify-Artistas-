
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class ListenerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    favorite_genres = models.TextField(blank=True, null=True)  # Géneros favoritos
    date_of_birth = models.DateField(blank=True, null=True)  # Fecha de nacimiento

class PlaybackHistory(models.Model):
    listener = models.ForeignKey(ListenerProfile, on_delete=models.CASCADE)
    song = models.ForeignKey('music.Song', on_delete=models.CASCADE)  # Relación con canciones
    playback_date = models.DateTimeField(auto_now_add=True)  # Fecha y hora de reproducción
