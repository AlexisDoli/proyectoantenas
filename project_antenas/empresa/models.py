# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Empresa(models.Model):

    nombre = models.CharField(max_length = 50 )
    contacto = models.CharField(max_length = 150)
    direccion = models.CharField(max_length = 250)
    telefono = models.CharField(max_length = 12)
    radiobases = models.IntegerField
    antenas = models.ImageField

    def __str__(self):
        pass