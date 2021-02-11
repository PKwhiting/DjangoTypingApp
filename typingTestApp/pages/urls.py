# pages/urls.py
from django.views.generic import TemplateView
from django.urls import path
from .views import HomePageView
from .views import AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('css/small.css', TemplateView.as_view(
        template_name='small.css',
        content_type='text/css')
    )
]