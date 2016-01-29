from django.conf.urls import patterns, include, url
from django.contrib import admin
from potolki import views
from home.views import FeedbackView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
	url(r'^contact/$', views.ContactView.as_view(), name='contact'),
	url(r'^ceilings/', include('ceilings.urls', namespace="ceilings")),
	url(r'^prices/', include('prices.urls', namespace="prices")),
	url(r'^calculator/', include('calculator.urls', namespace="calculator")),
	url(r'^gallery/', include('gallery.urls', namespace="gallery")),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
