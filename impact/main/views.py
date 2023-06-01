from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView

from rest_framework.generics import ListAPIView

from .models import FAQ
from .forms import ContactForm
from .utils.validators import VisitingValidator
from .serializers import FAQSerializer


class HomePageView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        VisitingValidator(request=request).check()

        context['title'] = 'Impact'

        return self.render_to_response(context)


class FAQView(ListView):
    model = FAQ
    template_name = 'main/faq.html'
    extra_context = {
        'title': 'FAQ'
    }


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'main/contact.html'
    extra_context = {
        'title': 'Contact us'
    }

    def form_invalid(self, form):
        for field in form.errors:
            messages.error(form.request, form.errors[field].as_text())
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


class FAQAPIView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
