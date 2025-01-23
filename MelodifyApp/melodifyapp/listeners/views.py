from django.shortcuts import render, get_object_or_404
from .models import Playlist

def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'listeners/playlist_list.html', {'playlists': playlists})

def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, id=playlist_id)
    return render(request, 'listeners/playlist_detail.html', {'playlist': playlist})
