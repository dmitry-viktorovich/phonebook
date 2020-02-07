from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Contact(models.Model):
    mobile_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=30)