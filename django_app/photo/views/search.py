from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404

from ..forms import PhotoAdd, PhotoAddMulti
from ..models import Photo, PhotoLike, PhotoDislike, Album

__all__ = [
    'photo_search',
]


def photo_search(request):
    albums = Album.objects.all()
    if request.method == 'GET':
        search_query = request.GET.get('search_box')
        all_photo = Photo.objects.filter(title__contains=search_query)
    else:
        all_photo = Photo.objects.all().order_by('-created_date')

    paginator = Paginator(all_photo, 16)

    page = request.GET.get('page')
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    context = {
        'albums': albums,
        'photos': photos,
        'user': request.user,
    }

    return render(request, 'photo/photo_list.html', context)