# music/views.py
from django.shortcuts import render, get_object_or_404
from .models import Song

# Vista para listar todas las canciones
def song_list(request):
    songs = Song.objects.all()  # Obtener todas las canciones de la base de datos
    return render(request, 'music/song_list.html', {'songs': songs})

# Vista para ver los detalles de una canción
def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)  # Obtener la canción por ID o devolver 404 si no existe
    return render(request, 'music/song_detail.html', {'song': song})
