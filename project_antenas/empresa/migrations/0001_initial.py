# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=12)),
            ],
        ),
    ]
