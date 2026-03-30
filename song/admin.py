from django.contrib import admin
from .models import Songs,Tag,SongTag
# Register your models here.
admin.site.register([SongTag,Songs,Tag])