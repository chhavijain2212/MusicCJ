from django.views import generic
from .models import *
from django.shortcuts import render, redirect
from django.db.models import Q


class IndexViewA(generic.ListView):
    template_name = 'music/indexa.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.order_by('title')


class IndexViewS(generic.ListView):
    template_name = 'music/indexs.html'
    context_object_name = 'songs'

    def get_queryset(self):
        return Song.objects.order_by('-likes')


class DetailViewA(generic.DetailView):
    model = Album
    template_name = 'music/detaila.html'
    context_object_name = 'a'


def search(request):
    albums = Album.objects.all()
    a1=albums
    songs = Song.objects.all()
    s1=songs
    query = request.GET.get("q")
    if query:
        words=query.split()
        a1 = (Album.objects.all()).filter(
            Q(title__icontains=words[0]) |
            Q(artist__icontains=words[0])
        ).distinct()
        s1 = (Song.objects.all()).filter(
            Q(title__icontains=words[0])
        ).distinct()
        for w in words:
            a= (Album.objects.all()).filter(
                Q(title__icontains=w) |
                Q(artist__icontains=w)
            ).distinct()
            s= (Song.objects.all()).filter(
                Q(title__icontains=w)
            ).distinct()
            a1=a|a1
            s1=s|s1
        return render(request, 'music/both.html', {
            'albums': a1,
            'songs': s1,
        })
    else:
        return render(request, 'music/both.html', {'albums': albums[:4], 'songs': songs.order_by('-likes')[:10]})


def likes(request,sid):
    try:
        s=Song.objects.get(pk=sid)
    except:
        return render(request, 'music/detaila.html', {'a':s.album})
    s.likes+=1
    s.save()
    return render(request, 'music/detaila.html', {'a': s.album})

