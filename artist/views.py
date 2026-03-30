from django.shortcuts import render,redirect
from .models import Artist
from .selectors import get_artist_by_id
from .forms import Artist_register,Artist_update
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def artist_update_view(request):
    user=get_artist_by_id( request.user)

    if user:
        form=Artist_update(request.POST)
        Artist.objects.update_artist(user,form.cleaned_data)
        return render(request,'dashboard.html',{'user':request.user})
    else:
        form=Artist_update()
        return render(request,'dashboard.html',{'form':form ,'user':user})
    
        
        

