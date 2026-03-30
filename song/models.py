from django.db import models
import uuid
from artist.models import Artist
# Create your models here.
class Tag(models.Model):
    name=models.CharField(unique=True,max_length=30)

    def save(self,*args, **kwargs):
        self.name=self.name.lower().strip()
        super().save(*args, **kwargs)
    
class Songs(models.Model):
    id=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    title=models.CharField(max_length=300)
    artist=models.ForeignKey(Artist,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    is_private=models.BooleanField(default=False)
    file=models.FileField(upload_to='uploads/')
    tags=models.ManyToManyField(Tag,through='SongTag')
    class Meta:
        unique_together=['title','artist']
    def __str__(self):
        return self.title


    
class SongTag(models.Model):
    song=models.ForeignKey(Songs,on_delete=models.CASCADE)
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
    added_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together=['song_id','tag']

    def __str__(self):
        return self.song.title