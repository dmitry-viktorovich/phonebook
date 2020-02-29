from django.db import models

class Person(models.Model):
    givenname = models.CharField(max_length=255, blank=True)
    surname = models.CharField(max_length=255, blank=True)
    othername = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=255, blank=True)
    telephoneNumber = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    mail = models.EmailField(max_length=255, blank=True)