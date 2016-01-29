# -*- coding: utf-8 -*-
from django.views.generic.edit import CreateView
from home.models import Feedback
from home.forms import FeedbackForm
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
		messages.success(self.request, 'Ваша заявка успешно отправлена!')
		return super(FeedbackView, self).form_valid(form)
    
