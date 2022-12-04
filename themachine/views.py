from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView

from .models import TextBlock


# Create your views here.
class TextBlockCreateView(CreateView):
    model = TextBlock
    fields = ['text']
    template_name = "themachine/textblock_form.html"

    def get_success_url(self):
        return reverse("home")



class HomeView(ListView):
    template_name = "themachine/home.html"
    model = TextBlock
    queryset = TextBlock.objects.all().order_by('-id')[:10]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

