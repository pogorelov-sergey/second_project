from django.views.generic import TemplateView
from gallery.models import Gallery, Picture
from django.views.generic.detail import DetailView
from ceilings.models import Ceiling
from django.shortcuts import render


class GalleryView(TemplateView):
    template_name = 'gallery/gallery.html'
    
    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context['gallerys'] = Gallery.objects.all()
        context['ceilings'] = Ceiling.objects.all()
        return context
        
def detail(request, pk):
	ceilings = Ceiling.objects.all()
	pictures = Picture.objects.filter(gallery__slug=pk)
	title = Gallery.objects.get(slug=pk)

	return render(request, 'gallery/picture.html', {'pictures': pictures, 'ceilings': ceilings, 'title': title})
        
'''       
class PictureDetailView(DetailView):
	model = Gallery
	template_name = 'gallery/picture.html'
	
	def get_context_data(self, **kwargs):
		context = super(PictureDetailView, self).get_context_data(**kwargs)
		context['pictures'] = Picture.objects.filter(gallery = self.object)
		context['ceilings'] = Ceiling.objects.all()
		return context
'''
