from django import forms
from .models import Playlists

class CreateForm(forms.ModelForm):
    
    class Meta:
        model = Playlists
        fields = ['title','private']
    

class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = Playlists
        fields = ['title','private']
