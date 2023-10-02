from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import pandas as pd
import json
from . import models

# Create your views here.
def say_hello(request):
    return render(request, 'hello.html', { 'name': 'Ben'})

# def display_restaurants(request):
#     return render(request, 'data.html', { 'zipcode': '07039' })

class HomePageView(TemplateView):
    template_name = "index.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class DataPageView(TemplateView):
    def get(self, request, **kargs):
        df = pd.read_csv('./restaurants/zipcodes/07039.csv')
        return render(request, 'data.html', {'restaurants': df.to_dict(orient='records')})
    
def search(request):
    if request.method == 'POST':
        zip = request.POST.get('textfield', None)
        zip_path = "./restaurants/zipcodes/" + zip + ".csv"
        try:
            df = pd.read_csv(zip_path)
        except:
            try: 
                # models.search_restaurants(zip)
                df = pd.read_csv(zip_path)
            except:
                return HttpResponse("no results found")
        return render(request, 'data2.html', {'restaurants': df.to_dict(orient='records')})
    else:
        return HttpResponse("not post")
    
def review(request):
    if request.method == 'POST':
        return
    else:
        return