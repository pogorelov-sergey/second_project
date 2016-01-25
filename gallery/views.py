from django.views.generic import TemplateView
from gallery.models import Gallery, Picture
from django.views.generic.detail import DetailView
from ceilings.models import Ceiling


class GalleryView(TemplateView):
    template_name = 'gallery/gallery.html'
    
    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context['gallerys'] = Gallery.objects.all()
        context['ceilings'] = Ceiling.objects.all()
        return context
        
       
class PictureDetailView(DetailView):
	model = Gallery
	template_name = 'gallery/picture.html'
	
	def get_context_data(self, **kwargs):
		context = super(PictureDetailView, self).get_context_data(**kwargs)
		context['pictures'] = Picture.objects.filter(gallery = self.object)
		context['ceilings'] = Ceiling.objects.all()
		return context
