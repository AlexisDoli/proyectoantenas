# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Antena

# Create your views here.

def antena_list(request):
    antenas = Antena.objects.all()
    context = {
        "antenas": antenas
    }
    return render(request, "mostrar_antenas.html", context)