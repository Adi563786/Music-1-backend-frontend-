from artist.models import Artist
from .models import Songs
from django.http import JsonResponse

def upload_song():
    pass

def add_song(artist,title,private):
    exists=Songs.objects.filter(artist,title).exists()
    if exists:
        return JsonResponse ({'message':"Song already exist with same title "})
    else:
        upload_song()
        song=Songs(artist,title=title,is_private=private)
        
        return JsonResponse({"message":"Song uploaded and added successfully "})
