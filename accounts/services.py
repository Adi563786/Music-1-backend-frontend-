# here we write our all buisness logic to let the views file look cleaner
from django.contrib.auth import authenticate
from .models import User
from artist.models import Artist

def register_user(data):

    user=User.objects.create_user(
        email=data['email'],
        password=data['password'],
        first_name=data['first_name'],
        middle_name=data['middle_name'],
        last_name=data['last_name'],
        is_artist=data['is_artist']
    )
    print(data["is_artist"])
    if data['is_artist']:Artist.objects.create_artist(user=user)
    return user
def login_user(request,email,password):
    user=authenticate(request,username=email,password=password)
    return user