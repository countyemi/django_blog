from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
def index(request):
    #return HttpResponse('welcome')
    return render(request, 'base.html')

    #return HttpResponse('welcome')