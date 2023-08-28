
from django.urls import path, include
from .views import *
from django.contrib.sitemaps.views import sitemap

from django.views.generic.base import TemplateView

app_name = 'home'


urlpatterns = [  
    path('', home, name='home'),
    
]
