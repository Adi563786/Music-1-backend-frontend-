from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login , logout as auth_logout
from .forms import RegistrationForm, LoginForm
from .services import register_user,login_user
from .selectors import is_artist_by_email
# Create your views here.

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form=RegistrationForm(request.POST or None)
    if request.method=="POST" and form.is_valid():
        register_user(form.cleaned_data)
        messages.success(request,"User registered successfully")
        return redirect('login')
    return render(request,'register.html',{'form':form})



def login_view(request):
    if request.user.is_authenticated:
        # user=is_artist_by_email(request.user)
        # if 
        
        return redirect('dashboard')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = login_user(request, email, password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'User logged in successfully')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('login')


    
    