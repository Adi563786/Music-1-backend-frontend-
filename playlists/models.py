from django.db import models
from accounts.models import User
import uuid
# Create your models here.        
        


class Playlists(models.Model):
    creator=models.ForeignKey(User,on_delete=models.CASCADE,related_name='playlists')
    playlist_id=models.CharField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    title=models.CharField(max_length=254)
    private=models.BooleanField(default=False)
    class Meta:
        unique_together=['creator','title']
        indexes=[
            models.Index(fields=['creator']),
            models.Index(fields=['title'])
        ]
    def __str__(self):
        return self.creator.email


class SavedPlaylists(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    playlist=models.ForeignKey(Playlists,on_delete=models.CASCADE)
    added_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together=['user',"playlist"]
    def __str__(self):
        return self.user.email




