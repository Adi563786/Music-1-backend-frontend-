# here we perform our all querys of accounts
from .models import User
from artist.models import Artist

def get_user_by_email(email):
    return User.objects.filter(email=email).first()
def is_artist_by_email(user):
    return Artist.objects.filter(user=user).first()
def get_id(id):
    return User.objects.filter(id=id).exists()
