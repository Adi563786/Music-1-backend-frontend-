from .models import Songs

def search_song_by_title(song_title):
    return Songs.objects.filter(title=song_title).all()

