from django.db import models

from django.conf import settings
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
    img = models.ImageField(upload_to='photo')