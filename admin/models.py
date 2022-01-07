from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Brands(models.Model):
    brand = models.CharField(max_length=30)
    
