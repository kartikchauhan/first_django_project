from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'index.html', context)


def lists(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404('Album doesn\'t exist')
    return render(request, 'lists.html', {'album': album})

def favorite(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    try:
        selected_song = album.song_set.get(id=request.POST['song'])
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'lists.html', {'album': album})
    except Song.DoesNotExist:
        raise Http404("<h1>Song doesnt exist Homie</h1>")


