from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404

from ..forms import PhotoAdd, PhotoAddMulti, CommentAdd, PhotoEdit
from ..models import Photo, PhotoLike, PhotoDislike, Album

__all__ = [
    'photo_list',
    'photo_add',
    'photo_add_multi',
    'photo_like',
    'photo_detail',
    'photo_delete',
    'photo_edit',
]


def photo_list(request):

    # 엘범필터
    albums = Album.objects.all()
    sca = request.GET.get('sca')
    if sca == None:
        all_photo = Photo.objects.all().order_by('-created_date')
    else:
        all_photo = Photo.objects.filter(album__title=sca).order_by('-created_date')
    # 엘범필터 끝

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


@login_required
def photo_like(request, pk, like_type='like'):
    photo = get_object_or_404(Photo, pk=pk)
    user = request.user

    # like_type에 따라 모델을 선택
    like_model = PhotoLike if like_type == 'like' else PhotoDislike
    opposite_model = PhotoDislike if like_type == 'like' else PhotoLike

    # user가 클릭을 한 상태인가 확인
    user_like_exist = like_model.objects.filter(
        user=user,
        photo=photo,
    )

    # user가 클릭한 상태이면 객체 삭제
    if user_like_exist.exists():
        user_like_exist.delete()

    # user가 클릭한 상태가 아니면 객체 생성, 반대 객체 삭제
    else:

        like_model.objects.create(
            user=user,
            photo=photo,
        )
        opposite_model.objects.filter(
            user=user,
            photo=photo,
        ).delete()

    return redirect('photo:photo_list')


def photo_detail(request, pk):
    photo = Photo.objects.get(pk=pk)
    comments = photo.comment_set.order_by('-created_date')
    user = request.user
    form = CommentAdd()
    context = {
        'user': user,
        'photo': photo,
        'comments': comments,
        'form': form,
    }
    return render(request, 'photo/photo_detail.html', context)


def photo_delete(request, photo_pk):
    p1 = Photo.objects.get(pk=photo_pk)
    p1.img.crop['400x400'].delete()
    p1.img.delete()
    p1.delete()
    return redirect('photo:photo_list')


def photo_edit(request, photo_pk):
    photo = get_object_or_404(Photo, pk=photo_pk)
    if request.method == 'POST':
        form = PhotoEdit(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.title = form.cleaned_data['title']
            photo.description = form.cleaned_data['description']
            messages.success(request, '사진수정 성공')
            photo.save()
            return redirect('photo:photo_detail', pk=photo_pk)
    else:
        form = PhotoEdit(instance=photo)
        return render(request, 'photo/photo_add.html', {'form': form})