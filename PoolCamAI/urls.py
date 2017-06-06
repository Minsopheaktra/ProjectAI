from django.conf.urls import url

from . import views
from .camera import SnapShot

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^main/$', views.main, name='main'),
    url(r'^video/$', views.video_feed, name='video'),
    url(r'^snap/$', SnapShot().get_shot(), name='snap'),
]
