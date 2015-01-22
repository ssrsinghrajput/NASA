'''docstring for urls'''
from django.conf.urls import patterns, url, include
import views
from django.contrib.auth.decorators import login_required
urlpatterns = patterns('',
                       url(r'^newgrid/', views.Grid_form),
                       url(r'^newrover/', views.Rover_form),
                       url(r'^newsensor/', views.Rover_Sensor),
                       url(r'^newmineral/', views.Mineral1),
                       url(r'^$', views.menu),
                       url(r'^movement/', views.movementstring),
                       url(r'^roverupdate/', views.roverupdate1),
                       url(r'^login/', views.user_login),
                       url(r'^logout/', views.logout_view),
                       url(r'^register/', views.register),
                       url(r'^API/$', (views.Listallrovers.as_view())),
                       url(r'^API/(?P<pk>[0-9]+)/$',login_required(views.Allrovers.as_view())),
                       url(r'^API/ALL/',views.Allrovers1.as_view()),
                       url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
                       )
