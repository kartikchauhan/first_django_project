from django.http import HttpResponse


def index(request):
    return HttpResponse("this is my music app")


def lists(request, album_id):
    return HttpResponse("<h1>this is album no." + str(album_id) + "</h1>")
