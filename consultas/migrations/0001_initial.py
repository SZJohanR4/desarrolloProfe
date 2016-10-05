# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-05 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('crear_Usuario', models.CharField(max_length=100)),
                ('registrar_Informacion', models.CharField(max_length=100)),
                ('modificar_Informacion', models.CharField(max_length=100)),
                ('eliminar_Informacion', models.CharField(max_length=100)),
                ('crear_Proyecto', models.CharField(max_length=100)),
                ('realizar_Consulta_filtrada', models.CharField(max_length=100)),
                ('cambiar_archivos', models.CharField(max_length=100)),
                ('enviar_informes', models.CharField(max_length=100)),
                ('asignar_proyecto', models.CharField(max_length=100)),
            ],
        ),
    ]