# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_carmodels'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Страна изготовитель', max_length=20, default='Страна не выбрана')),
            ],
        ),
        migrations.CreateModel(
            name='Fotki',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('foto', models.ImageField(verbose_name='Фотография', upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='brands',
            name='brand',
            field=models.CharField(verbose_name='МАрка автомобиля', max_length=30),
        ),
        migrations.AlterField(
            model_name='carmodels',
            name='avto',
            field=models.ForeignKey(verbose_name='Модель аммвтомобиля', to='catalog.Brands'),
        ),
    ]
