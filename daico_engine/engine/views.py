from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
from django.shortcuts import render
 
def index(request):
    return render(request, 'user/home/home.html')
def favorite(request):
    return render(request, 'user/favorite/favorite.html')
def store(request):
    return render(request, 'user/notification/store.html')