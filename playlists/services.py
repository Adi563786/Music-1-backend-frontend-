from django.contrib.auth.decorators import login_required
from .models import Playlists
from .models import SavedPlaylists
from artist.models import Albums
from accounts.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .selectors import get_saved_playlist_obj


def user_create_playlist(user,title,isPrivate):
    try:
        playlist=Playlists.objects.get(title=title)
        return {"message":"Playlist exists with same title"}
    except:
        playlist=Playlists(creator=user,title=title,private=isPrivate)
        playlist.save()
        SPlaylists=SavedPlaylists(user=user,playlist=playlist)
        SPlaylists.save()
        return {"message":"Playlist created successfully"}


def user_update_playlists(user,playlist,**kwargs):
    if user!=playlist.creator:
        raise PermissionDenied("User has not permission for altering this playlist")
    for key,val in kwargs.items():
        setattr(playlist,key,val)
    playlist.save()
    return playlist


def user_delete_playlist(user,playlist):
    if user!=playlist.creator:
        raise PermissionDenied("User has not perimission to delete this playlist")
    saved_playlist=get_saved_playlist_obj(user,playlist)
    if not saved_playlist:return {"message":f'user have not any playlist named {playlist.title}'}
    playlist.delete()
    return {"message":"Playlist deleted successfully"}

def user_toggle_playlist(user,playlist):
    
    obj,created=SavedPlaylists.objects.get_or_create(
        user=user,
        playlist=Playlists
    )
    if not created:
        obj.delete()
        return {"message":"Playlist unsaved successfully"}
    return {"message":"Playlist saved successfully"}

def artist_create_album(artist,title , private):
    obj,created =Albums.objects.get_or_create(artist=artist,title=title,is_private=private)
    if not created:
        return {"message":"Album with same name exists already "}    
    return {"message":"album  created successfully"}

def get_all_album_of_artist(artist):
    data=Albums.objects.filter(artist=artist).all()    
    return {"myAlbums":data}
        
    

    




