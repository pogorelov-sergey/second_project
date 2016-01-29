from django.conf.urls import patterns, url
from prices import views


urlpatterns = patterns('',
    url(r'^$', views.PriceView.as_view(), name='price'),
)
