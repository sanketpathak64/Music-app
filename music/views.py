from django.shortcuts import render
from django.http import HttpResponse
from .models import Album,Song
from django.shortcuts import render
from django.http import Http404
# Create your views here.
def index(request):
    html=''
    all_albums=Album.objects.all()
    context={'all_albums':all_albums}
    return render(request,'music/index.html',context)

def detail(request,album_id):
    try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("We don't have it yet")
    return render(request,'music/detail.html',{'album':album})
