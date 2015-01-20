'''docstring for urls'''
from django.conf.urls import patterns, url
import views

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
                       url(r'^register/', views.register)
                       )
