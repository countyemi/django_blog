from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, 'login/index.html')

def signup(request):
    form=UserCreationForm()
    registered=False
    if request.method=='POST':
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered=True



    dict={'form':form,
          'registered':registered}
    return render(request, 'login/signup.html', context=dict)
def signin(request):
    form=AuthenticationForm
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('base_index'))
    return render(request, 'login/signin.html', context={'form':form})




