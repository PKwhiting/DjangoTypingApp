from django.views.generic import TemplateView
from .models import Text
from django.shortcuts import render, redirect
import random

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get(self,request):
        length = Text.objects.count()
        num = random.randint(1,length)
        print('tacos')
        item = Text.objects.get(id=num)
        context = {
            'text': item.text
        }
        return render(request, "../templates/home.html", context)

class AboutPageView(TemplateView):
    template_name = 'about.html'


