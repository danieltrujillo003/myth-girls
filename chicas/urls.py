from django.conf.urls import patterns, url
from chicas import views

urlpatterns = patterns('',
    url(r'^story/$', views.story, name='chicas'),
    )