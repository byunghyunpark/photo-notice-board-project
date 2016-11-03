from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from ..forms import PhotoAdd, PhotoAddMulti
from ..models import Photo

__all__ = [
    'photo_list',
    'photo_add',
    'photo_add_multi',
]


def photo_list(request):
    all_photo = Photo.objects.all().order_by('-created_date')

    context = {
        'all_photo': all_photo,
    }
    return render(request, 'photo/photo_list.html', context)

@login_required
def photo_add(request):
    if request.method == 'POST':
        form = PhotoAdd(request.POST, request.FILES)
        if form.is_valid():
            album = form.cleaned_data['album']
            owner = request.user
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            file = form.cleaned_data['file']

            Photo.objects.create(
                album=album,
                owner=owner,
                title=title,
                description=description,
                img=file,
            )
        messages.success(request, '사진등록 성공')
        return redirect('photo:photo_list')
    else:
        form = PhotoAdd()
    return render(request, 'photo/photo_add.html', {'form': form})



def photo_list(request):
    all_photo = Photo.objects.all().order_by('-created_date')

    context = {
        'all_photo': all_photo,
    }
    return render(request, 'photo/photo_list.html', context)


@login_required
def photo_add_multi(request):
    if request.method == 'POST':
        form = PhotoAddMulti(request.POST, request.FILES)
        if form.is_valid():
            album = form.cleaned_data['album']
            owner = request.user
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']

            files = request.FILES.getlist('file')
            for i, file in enumerate(files):
                Photo.objects.create(
                    album=album,
                    owner=owner,
                    title='%s(%s)' % (title, i+1),
                    description='%s(%s)' % (description, i+1),
                    img=file,
                )
            messages.success(request, '사진등록 성공')
            return redirect('photo:photo_list')
    else:
        form = PhotoAddMulti()
    return render(request, 'photo/photo_add.html', {'form': form})