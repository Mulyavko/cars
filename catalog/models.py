from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Country(models.Model):
    country_list = (
        ('США'),
        ("Германия"),
        ("Италия"),
        ("СССР"),
        ("Япония"),
        ("Корея"),
        ("Китай"), 
    )
    name = CharField(max_length=20, verbose_name= 'Страна изготовитель', default='')

    def __str__(self):
        return f"{self.id}: {self.name}"

class Brand(models.Model):
    brand = models.CharField(max_length=30, verbose_name= 'Марка автомобиля')
    '''
    strana = models.ForeignKey(Country,  on_delete=models.CASCADE)
    '''
    def __str__(self):
        return f"{self.id}: {self.brand}" 
class Fotki(models.Model):
    foto = models.ImageField(verbose_name='Фотография')

    def __str__(self):
        return f"{self.foto}:"

class CarModel(models.Model):
    avto = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Модель автомобиля')
    '''
    carmodel = models.CharField(max_length=20, on_delete=CASCADE) 
    '''
    carmodel = models.CharField(max_length=20, null=False) 
    '''
    foto = models.ForeignKey(Fotki, on_delete=CASCADE)
    '''
    def __str__(self):
        return f"{self.id}: {self.brand}: {self.carmodel}, {self.foto}"



        




    
