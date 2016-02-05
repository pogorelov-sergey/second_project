from django.conf.urls import patterns, url
from gallery import views


urlpatterns = patterns('',
    url(r'^$', views.GalleryView.as_view(), name='gallery'),
    url(r'^(?P<pk>\w+)/$', views.detail, name='picture'),
)
