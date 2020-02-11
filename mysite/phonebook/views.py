# from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from phonebook.models import Person, Contact

def index(request):
    person = Person.objects.all()
    contact = Contact.objects.all()
    args = {'persons':person, 'contacts':contact}
    return render(request, 'persons/persons.html', args)
