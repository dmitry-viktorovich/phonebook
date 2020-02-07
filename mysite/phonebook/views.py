# from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from phonebook.models import Person


def index(request):
    return render(request, 'persons/persons.html')
