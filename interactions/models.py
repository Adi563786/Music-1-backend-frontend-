from django.db import models
from accounts.models import User
from artist.models import Artist
# Create your models here.
class Follows(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following_artist')
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE,related_name='followers')
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together =('user','artist')