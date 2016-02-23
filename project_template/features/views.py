from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect

from .models import *
from .forms import *


class NewFeatureRequestView(FormView):
    template_name = "features/new_request.html"
    form_class = NewFeatureRequestForm

    def form_valid(self, form):
        self.instance = form.save(self.request.user)
        return super(NewFeatureRequestView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("new-feature-request-added",
            args=[self.instance.pk, self.instance.slug])


class FeatureRequestView(TemplateView):
    template_name = "features/request.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FeatureRequestView, self).get_context_data(*args, **kwargs)
        context['feature_request'] = get_object_or_404(FeatureRequest, pk=kwargs['pk'])
        return context

class NewFeatureRequestSuccessView(TemplateView):
    template_name = "features/request_added_success.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewFeatureRequestSuccessView, self).get_context_data(*args, **kwargs)
        context['pk'] = kwargs['pk']
        context['slug'] = kwargs['slug']
        return context


def home_view(request):
    return redirect(reverse("new-feature-request"))