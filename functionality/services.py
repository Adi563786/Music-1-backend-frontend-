from rest_framework.views import APIView
from rest_framework.response import Response
from artist.models import Artist
from accounts.models import User
from song.models import Songs,SongTag,Tag
from django.db import transaction,IntegrityError
from celery import shared_task
import time , os
from django.core.files import File

class SearchView(APIView):
    def get(self,request):
        q=request.GET.get('q')
        users=Artist.objects.filter(stage_name__istartswith=q)
        data=[
            {'artist':u.stage_name} for u in users
        ]
        return Response(data=data)
    
def get_song_by_artist(artist):
    song=Songs.objects.filter(artist=artist)    
    return song
def get_song_by_title(title):
    song=Songs.objects.filter(title=title)
    return song


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5, max_retries=3)
def upload_song_by_artist(self, email, title, full_path, tags):
    try:
        print("Task started")

        time.sleep(5)

        with transaction.atomic():
            user = User.objects.filter(email=email).first()
            if not user:
                raise Exception("User not found")

            artist = Artist.objects.filter(user=user).first()
            if not artist:
                raise Exception("Artist not found")

            with open(full_path, 'rb') as f:
                song_file = File(f, name=os.path.basename(full_path))

                song = Songs.objects.create(
                    artist=artist,
                    title=title,
                    file=song_file
                )

            for tag in tags:
                tag_instance, _ = Tag.objects.get_or_create(name=tag)
                SongTag.objects.get_or_create(song=song, tag=tag_instance)

        # ✅ cleanup
        if os.path.exists(full_path):
            os.remove(full_path)

        return {"status": "success", "song_id": song.id}

    except IntegrityError:
        return {"status": "error", "message": "Song already exists"}

    except Exception as e:
        raise self.retry(exc=e)