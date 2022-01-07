from django.contrib import admin

# Register your models here.
from .models import Brands, CarModels, Fotki, Country

admin.site.register(Brands)
admin.site.register(CarModels)
admin.site.register(Country)
admin.site.register(Fotki)





