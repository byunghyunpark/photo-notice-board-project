from django.conf.urls import url

from photo import views


urlpatterns = [
    url(r'^$', views.photo_list, name='photo_list'),
]
