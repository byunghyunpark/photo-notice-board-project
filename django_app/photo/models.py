from django.db import models

from django.conf import settings
from versatileimagefield.fields import VersatileImageField

from mysite.utils.models import BaseModel


class Album(BaseModel):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title


class Photo(BaseModel):
    album = models.ForeignKey(Album)
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    img = VersatileImageField(
        'Image',
        upload_to='photo/'
    )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PhotoLike', related_name='photo_set_like_users')
    dislike_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='PhotoDislike', related_name='photo_set_dislike_users')

    def __str__(self):
        return self.title


class PhotoLike(BaseModel):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class PhotoDislike(BaseModel):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
