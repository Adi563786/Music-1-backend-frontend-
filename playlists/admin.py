from django.contrib import admin
from .models import Playlists,SavedPlaylists
# Register your models here.
admin.site.register(Playlists)
admin.site.register(SavedPlaylists)