from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.photo_list, name='photo_list'),
    url(r'^photo/add/$', views.photo_add, name='photo_add'),
    url(r'^photo/add/multi/$', views.photo_add_multi, name='photo_add_multi'),
]
