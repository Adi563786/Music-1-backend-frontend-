from django.urls import path

from .views import update_playlist,delete_playlist,create_playlist,toggle_save_unsave_playlist,album_create,album_view

urlpatterns = [
    path('create/',create_playlist,name='create_playlist'),
    path('update/',update_playlist,name='update_playlist'),
    path('delete/',delete_playlist,name='delete_playlist'),
    path('toggle/',toggle_save_unsave_playlist,name='toggle_playlist'),
    path('album/',album_view,name='albumview'),
    path('createalbum/',album_create,name='artist_create_album')
]
