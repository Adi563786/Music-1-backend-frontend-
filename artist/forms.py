from django import forms
from .models import Artist,Albums



class Artist_register(forms.ModelForm):
    class Meta:
        model=Artist
        fields=["stage_name",'genre']
class Artist_update(forms.ModelForm):
    
    class Meta:
        model =Artist
        fields = ['stage_name','genre']




    