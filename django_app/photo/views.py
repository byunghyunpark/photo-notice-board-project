from django.shortcuts import render, redirect
from django.http import HttpResponse

def photo_list(request):
    return render(request, 'photo/photo_list.html', {})