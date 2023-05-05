from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json

# Create your views here.
with open('/home/student/Projects/DjangoCountries/countries.json') as f:
    f_countries = json.load(f)
list_countries = []
list_lang = ['English']
for item in f_countries:
    list_countries.append(item['country'])
    for lang in item['languages']:
        if not list_lang.count(lang):
            list_lang.append(lang)
countries = sorted(list_countries)
languages = sorted(list_lang)


def home(request):
    context = {
        "name": "Irina",
        "surname": "Stoliarova",
    }
    return render(request, 'index.html', context)

def countries_list(request):
    context = {
        "countries": countries
    }
    return render(request, 'countries-list.html', context)

def languages_list(request):
    context = {
        "languages": languages
    }
    return render(request, 'languages.html', context)

def get_country(request, name):
    for country in countries:
        if country == name:
            context = {
                'country': country
            }
            return render(request, 'country_page.html', context)
    return HttpResponseNotFound(f"Страна с таким именем не найдена")