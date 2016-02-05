from django.conf.urls import patterns, url
from ceilings import views


urlpatterns = patterns('',
    url(r'^(?P<pk>\w+)/$', views.detail, name='detail'),
)
