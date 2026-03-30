from django.urls import path
from .views import upload_file,get_songs_artist
urlpatterns = [
    path("uploadsong/",upload_file,name='uploadsong'),
    path('mySongs/',get_songs_artist,name='mySongs')
]
