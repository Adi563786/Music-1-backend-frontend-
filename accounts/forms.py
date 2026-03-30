from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['email', 'first_name', 'middle_name','last_name', 'password','is_artist']

    def clean_email(self):
        email=self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("email already exists")
        return email
    

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
