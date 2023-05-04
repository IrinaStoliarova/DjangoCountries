from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Добро пожаловать! Скоро здесь что-то будет')
