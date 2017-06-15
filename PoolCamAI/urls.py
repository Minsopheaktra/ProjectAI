from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^main/$', views.main, name='main'),
    url(r'^video/$', views.video_feed, name='video'),
    url(r'^snap/$', views.snap, name='snap'),
    url(r'^notify/$', views.notification_view, name='notify'),
    url(r'^dashboard/(?P<cam_no>[0-9])$', views.dashboard, name='dashboard'),
]
