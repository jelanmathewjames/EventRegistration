from django.db import models

# Create your models here.
class RegistrationForm(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10,unique=True)
    current_education = models.CharField(max_length=20)
    institution = models.CharField(max_length=20)