from django.shortcuts import render, redirect
from django.http import HttpResponse

from ..models import Photo

__all__ = [
    'photo_list',
]

def photo_list(request):
    all_photo = Photo.objects.all().order_by('-created_date')

    context = {
        'all_photo': all_photo,
    }

    return render(request, 'photo/photo_list.html', context)