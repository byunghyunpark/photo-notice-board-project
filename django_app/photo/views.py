from django.shortcuts import render
from django.http import HttpResponse

def album_list(request):
    return render(request, 'photo/album_list.html', {})