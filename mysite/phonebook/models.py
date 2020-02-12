from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    mobile_number = models.CharField(max_length=11, blank=True)
    extension_number = models.IntegerField(blank=True)
    department = models.CharField(max_length=30, blank=True)
    department_position = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=30, blank=True)


    def __str__(self):
        return self.first_name