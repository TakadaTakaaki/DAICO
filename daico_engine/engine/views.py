from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse
from django.shortcuts import render
 
def index(request):
    return render(request, 'for-user/html/home/before-login.html')
def favorite(request):
    return render(request, 'for-user/html/favorite/favorite.html')
def store(request):
    return render(request, 'for-user/html/notification/store.html')