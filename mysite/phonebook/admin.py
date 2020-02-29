from django.contrib import admin
from phonebook.models import Person



class PersonAdmin(admin.ModelAdmin):
    list_display=('givenname', 'othername', 'surname', 'company', 'department', 'mobile', 'telephoneNumber', 'title', 'mail')
    list_display_links = ('givenname', 'othername')
    list_editable=('surname', 'company', 'department', 'mobile', 'telephoneNumber', 'title', 'mail')

admin.site.register(Person, PersonAdmin)
