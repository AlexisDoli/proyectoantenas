# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from rest_framework.response import Response
from .serializers import Rb_serial

from .models import Radiobase
from rest_framework.views import APIView

# Create your views here.

def rb_list(request):
    radiobases = Radiobase.objects.all()
    context = {
        "radiobases": radiobases
    }
    return render(request, "mostrar_rb.html", context)

class Api_rb_list(APIView):
    def get(self, request):
        radiobases = Radiobase.objects.all()
        data = Rb_serial(radiobases, many = True)
        return Response(data.data)