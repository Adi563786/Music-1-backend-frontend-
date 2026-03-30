from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from artist.models import Artist,Albums
from .services import user_create_playlist,user_delete_playlist,user_toggle_playlist,user_update_playlists,artist_create_album,get_all_album_of_artist
from .selectors import get_playlist_object,get_saved_playlist_obj
# from .forms import CreateForm,UpdateForm
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.

@login_required
def create_playlist(request):
    if request.method=='POST':
        user=request.user
        title=request.POST.get('title')
        private=False if request.POST.get("visibility")=='public' else True
        data=user_create_playlist(user,title,private)
        return JsonResponse(data=data)
    return JsonResponse(data={'message':"Some error occured"})


@login_required
def update_playlist(request):
    dic=request.POST.dict()
    user=request.user
    title=dic['title']
    playlist=get_playlist_object(user,title)
    data={}
    if playlist:
        data=user_update_playlists(user,playlist,dic)
        JsonResponse(data={'message':"playlist updated"})
    else:
        return JsonResponse(data={'message':"playlist not found"})
@login_required
def delete_playlist(request):
    title=request.POST.get('title')
    user=request.user
    playlist=get_playlist_object(user,title)
    data=user_delete_playlist(user,playlist)
    return JsonResponse(data=data)
@login_required
def toggle_save_unsave_playlist(request):
    title=request.POST.get('title')
    user=request.user
    playlist=get_playlist_object(user,title)
    data=user_toggle_playlist(user,playlist)
    return JsonResponse(data=data)

@login_required
def album_create(request):
    data=request.POST.dict()
    title=data['title']
    private=False if request.POST.get("visibility")=='public' else True
    artist=Artist.objects.filter(user=request.user).first()
    if not artist:return JsonResponse({"message":"only an artist can create an album please enroll for artist first"})
    data=artist_create_album(artist,title,private)
    print(data)
    return JsonResponse (data=data)

@login_required
def album_view(request):
    id=request.GET.get('id')
    if id:
        artist=Artist.objects.filter(user=request.user).first()
        album=Albums.objects.filter(id=id,artist=artist).first()
        
        return render(request,'particular_album.html',{'artist_album':album})
        pass
    else:
        artist=Artist.objects.filter(user=request.user).first()
        if not artist:return JsonResponse({"message":"only an artist can create an album please enroll for artist first"})
        data=get_all_album_of_artist(artist)
        return render(request,'album.html',data)



    

    
    
    
