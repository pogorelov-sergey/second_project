from django.conf.urls import patterns, url
from gallery import views


urlpatterns = patterns('',
    url(r'^$', views.GalleryView.as_view(), name='gallery'),
    url(r'^(?P<pk>\d+)/$', views.PictureDetailView.as_view(), name='picture'),
)
