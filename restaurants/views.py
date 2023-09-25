from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import json

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
        f = open('./restaurants/zipcodes/07039_all.json')
        data = json.load(f)
        f.close()
        return render(request, 'data.html', data)
    
def search(request):
    if request.method == 'POST':
        zip = request.POST.get('textfield', None)
        try:
            zip_path = "./restaurants/zipcodes/" + zip + ".json"
            f = open(zip_path)
            data = json.load(f)
            f.close()
            return render(request, 'data2.html', data)
        except:
            print("ben error")
            return HttpResponse("none")
    else:
        return HttpResponse("not post")
    