from .models import Artist

def get_artist_by_id(id):
    return Artist.objects.get(id=id).first()