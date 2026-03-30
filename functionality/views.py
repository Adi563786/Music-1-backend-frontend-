from django.shortcuts import render
from artist.models import Artist
# Create your views here.
def SearchArtistView(request):
    q=request.GET.get('q')
    users = Artist.objects.filter(stage_name__istartswith=q)
        
    data = [
        {"id": u.stage_name, 'genre':u.genre,'monthly_listener':u.monthly_listeners,
         'verified':u.verified,'total_streams':u.total_streams,'total_followers':u.total_followers}
        for u in users
    ]
    return render(request,'artist.html',{"data":data})