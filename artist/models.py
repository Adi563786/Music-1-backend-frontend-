from django.db import models
from accounts.models import User
import uuid

class ArtistManager(models.Manager):
    def create_artist(self, **kwargs):
        artist = self.model(**kwargs)
        artist.save()
        return artist

    def update_artist(self, artist_id, **kwargs):
        artist = self.get(id=artist_id)
        for key, value in kwargs.items():
            setattr(artist, key, value)
        artist.save()
        return artist


class Artist(models.Model):
    GENRE_CHOICES = [
        ('pop', 'Pop'),
        ('rock', 'Rock'),
        ('hiphop', 'Hip Hop'),
        ('jazz', 'Jazz'),
        ('classical', 'Classical'),
        ('edm', 'EDM'),
        ('lofi', 'Lo-fi'),
        ('metal', 'Metal'),
        ('indie', 'Indie'),
        ('folk', 'Folk'),
        ('blues', 'Blues'),
        ('reggae', 'Reggae'),
        ('country', 'Country'),
        ('kpop', 'K-Pop'),
        ('latin', 'Latin'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stage_name = models.CharField(max_length=100, default="")
    verified = models.BooleanField(default=False)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=20)
    monthly_listeners = models.IntegerField(default=0)
    total_streams = models.IntegerField(default=0)
    total_followers=models.IntegerField(default=0)
    objects = ArtistManager()

    def __str__(self):
        return self.user.email
    
class Albums(models.Model):
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    id=models.CharField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_private=models.BooleanField(default=False)


    class Meta:
        unique_together=['title','artist']

    def __str__(self):
        return self.title
    
    
