from django.views.generic import TemplateView
from .models import Text
from django.shortcuts import render, redirect

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get(self,request):
        item = Text.objects.get(id=1)
        context = {
            'text': item.text
        }
        return render(request, "../templates/home.html", context)

class AboutPageView(TemplateView):
    template_name = 'about.html'


