from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from artist.models import Artist
from functionality.services import get_song_by_artist,upload_song_by_artist
from django.contrib import messages
from django.core.files.storage import default_storage
import os
from django.conf import settings
# Create your views here.
@login_required
def upload_file(request):
    if request.method == "POST":
        tags = request.POST.getlist('tags') 
        title = request.POST.get('title').lower()
        song_file = request.FILES.get('song_file')
        artist = Artist.objects.filter(user=request.user).first()
        if not artist:
            return JsonResponse({"message": "You are not an artist. Please register first."}, status=403)
        if not song_file:
            return JsonResponse({"message": "No file recieved"}, status=403)
        #save temporarily 
        temp_path=default_storage.save(f'temp/{artist.user.id}+{song_file.name}',song_file)
        full_path=os.path.join(settings.MEDIA_ROOT ,temp_path)
        task = upload_song_by_artist.delay(artist.user.email, title, full_path, tags)
        print(task.id)
        return JsonResponse({
            'status': 'success', 
            'message': 'upload started successfully!'
        })

    # If GET request, just show the page
    return render(request, 'song.html')
    


@login_required
def get_songs_artist(request):
    artist=Artist.objects.filter(user=request.user).first()
    if not artist:
        return JsonResponse ({"message":"Only Artist can have songs and u are not an artist"})
    else:
        song=get_song_by_artist(artist)
        return render(request,'song.html',{'mySongs':song})



