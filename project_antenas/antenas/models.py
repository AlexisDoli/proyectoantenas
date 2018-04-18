# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Antena(models.Model):
    
    aplicacion = models.CharField(max_length = 250)
    frecuencia_op = models.CharField(max_length = 50 )
    empresaduena = models.CharField(max_length = 150)
    marca = models.CharField(max_length = 150)
    modelo_antena = models.CharField(max_length = 150)
    
    def __unicode__(self):
        return "{} {}".format(self.aplicacion, self.frecuencia_op, self.empresaduena, self.marca, self.modelo_antena)