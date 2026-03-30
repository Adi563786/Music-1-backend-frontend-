from .models import Playlists,SavedPlaylists
from accounts.models import User

def get_playlist_object(user, title):
    return Playlists.objects.filter(creator=user, title=title).first()

def get_saved_playlist_obj(user,playlist):
    return SavedPlaylists.objects.filter(user=user,playlist=playlist).first()

