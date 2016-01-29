from django.conf.urls import patterns, url
from calculator import views


urlpatterns = patterns('',
    url(r'^$', views.calculator, name='calculator'),
)
