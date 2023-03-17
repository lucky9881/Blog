from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=123)
    email = models.CharField(max_length=123)
    phone = models.CharField(max_length=12)
    msg = models.CharField(max_length=123)
    date = models.DateField()