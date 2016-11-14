from django.conf.urls import url
from ..views import photo_list
from .. import views
urlpatterns = [
    # url(r'^photo/list/$', photo_list, name='photo_list'),
    url(r'^photo/$', views.PhotoList.as_view(), name='photo_list'),
    url(r'^photo/add/$', views.PhotoAdd.as_view(), name='photo_add'),
]