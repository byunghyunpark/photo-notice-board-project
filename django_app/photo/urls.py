from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.photo_list, name='photo_list'),
    url(r'^photo/add/$', views.photo_add, name='photo_add'),
    url(r'^photo/add/multi/$', views.photo_add_multi, name='photo_add_multi'),
    url(r'^photo/(?P<pk>[0-9]+)/(?P<like_type>\w+)/$', views.photo_like, name='photo_like'),
    url(r'^photo/(?P<pk>[0-9]+)/$', views.photo_detail, name='photo_detail'),
    url(r'^photo/(?P<pk>[0-9]+)/comment/add/$', views.add_comment, name='add_comment'),
    url(r'^photo/search/$', views.photo_search, name='photo_search'),
    url(r'^photo/(?P<photo_pk>[0-9]+)/comment/delete/(?P<comment_pk>[0-9]+)/$', views.comment_delete, name='comment_delete'),
    url(r'^photo/(?P<photo_pk>[0-9]+)/comment/edit/(?P<comment_pk>[0-9]+)/$', views.comment_edit, name='comment_edit'),
    url(r'photo/(?P<photo_pk>[0-9]+)/delete', views.photo_delete, name='photo_delete'),
    url(r'photo/(?P<photo_pk>[0-9]+)/edit', views.photo_edit, name='photo_edit'),
]