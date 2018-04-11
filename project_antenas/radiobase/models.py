# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Radiobase(models.Model):

    altura = models.CharField(max_length = 12)
    empresaduena = models.CharField(max_length = 50 )
    direccion = models.CharField(max_length = 250)
    coordenadas = models.CharField(max_length = 250)

    def __str__(self):
        pass