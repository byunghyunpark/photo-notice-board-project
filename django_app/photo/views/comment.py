from django.contrib import messages
from django.shortcuts import redirect

from ..models import Photo, Comment

__all__ = [
    'add_comment',
    'comment_delete',
]

def add_comment(request, pk):
    if request.method == 'POST':
        photo = Photo.objects.get(pk=pk)
        owner = request.user
        content = request.POST['content']

        Comment.objects.create(
            photo=photo,
            owner=owner,
            content=content,
        )
        messages.success(request, '댓글을 달았습니다')
        return redirect('photo:photo_detail', pk=photo.pk)


def comment_delete(request, photo_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    messages.success(request, '댓글이 삭제되었습니다')
    return redirect('photo:photo_detail', pk=photo_pk)