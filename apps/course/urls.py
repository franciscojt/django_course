from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create/$', views.add),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^destroy/(?P<id>\d+)$', views.delete),
    url(r'^comments/(?P<id>\d+)$', views.message),
    url(r'^comments/create/(?P<id>\d+)$', views.create),
]
