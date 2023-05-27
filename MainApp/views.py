from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Country, Language
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
import string

LETTERS = list(string.ascii_uppercase)

def home(request):
    context = {
        "name": "Irina",
        "surname": "Stoliarova",
    }
    return render(request, 'index.html', context)


def countries_list(request):
    countries = Country.objects.all()
    paginator = Paginator(countries, 10)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    context = {
        "letters": LETTERS,
        "paginator": paginator,
        "page_object": page_object
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


def get_language(request, id):
    try:
        language = Language.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Языка с таким номером не существует")
    countries = Country.objects.filter(language__id=id)
    context = {
        "language": language,
        "countries": countries
    }
    return render(request, 'language_page.html', context)


def countries_by_letter(request, letter):
    countries_by_let = Country.objects.filter(name__startswith=letter)
    context = {
        "countries": countries_by_let,
        "letter": letter
    }
    return render(request, 'countries-byletter.html', context)