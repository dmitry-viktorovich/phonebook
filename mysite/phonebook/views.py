# from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from phonebook.models import Person

def index(request):
    person = Person.objects.all().order_by('surname')
    args = {'persons':person}
    return render(request, 'persons/persons.html', args)
