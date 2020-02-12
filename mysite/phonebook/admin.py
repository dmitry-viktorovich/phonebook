from django.contrib import admin
from phonebook.models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display=('first_name', 'last_name', 'department', 'mobile_number', 'extension_number', 'department_position', 'email')
    list_display_links = ('first_name', 'last_name')
    list_editable=('department', 'mobile_number', 'extension_number', 'department_position', 'email')

admin.site.register(Person, PersonAdmin)
