from django.views import generic
from .models import Album


class IndexView(generic.ListView):
    template_name = "index.html"

    def get_queryset(self):
        return Album.objects.all()

class ListView(generic.DetailView):
    model = Album
    template_name = "lists.html"



