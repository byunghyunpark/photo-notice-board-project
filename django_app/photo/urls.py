from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.photo_list, name='photo_list'),
    url(r'^photo/add/$', views.photo_add, name='photo_add'),
    url(r'^photo/add/multi/$', views.photo_add_multi, name='photo_add_multi'),
    url(r'^photo/(?P<pk>[0-9]+)/(?P<like_type>\w+)/$', views.photo_like, name='photo_like'),
    url(r'^photo/(?P<pk>[0-9]+)/$', views.photo_detail, name='photo_detail'),
    url(r'^photo/(?P<pk>[0-9]+)/delete/$', views.photo_delete, name='photo_delete'),
    url(r'^photo/(?P<pk>[0-9]+)/comment/add/$', views.add_comment, name='add_comment'),
]
