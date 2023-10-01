from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('web-home')
    else:
        form= UserCreationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html',{'title':'Profile'})