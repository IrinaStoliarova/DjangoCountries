from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Country, Language
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    context = {
        "name": "Irina",
        "surname": "Stoliarova",
    }
    return render(request, 'index.html', context)

def countries_list(request):
    countries = Country.objects.all()
    context = {
        "countries": countries
    }
    return render(request, 'countries-list.html', context)

def languages_list(request):
    languages = Language.objects.all()
    context = {
        "languages": languages
    }
    return render(request, 'languages.html', context)

def get_country(request, id):
    try:
        country = Country.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Страны с таким номером не существует")
    context = {
                "country": country,
                "languages": country.language.all()
            }
    return render(request, 'country_page.html', context)