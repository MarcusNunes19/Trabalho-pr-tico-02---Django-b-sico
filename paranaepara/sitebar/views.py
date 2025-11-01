from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic

# Create your views here.
def index(request):
    template = loader.get_template('sitebar/index.html')
    return HttpResponse(template.render())

# class Indexview(generic.list):
#     template_name = 'sitebar/index.html'