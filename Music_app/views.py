from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from accounts.selectors import is_artist_by_email
from artist.models import Artist

def is_artist_by_email(user):
    return Artist.objects.filter(user=user).first()

@login_required
def dashboard_view(request):
    artist=is_artist_by_email(request.user)
    if artist:print(artist.genre,artist.stage_name)
    return render(request,'dashboard.html',{'user':request.user,'artist':artist})

def home_view(request):
    return render(request,'home.html',{'user':request.user})
    if request.user:
        print(request.user)
        return render(request,'home.html',{'user':request.user})
    else:
        pass

def remove_like(request):
    print('mewo sdfjslj')