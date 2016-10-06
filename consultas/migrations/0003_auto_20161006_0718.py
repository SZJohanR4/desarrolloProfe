# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-06 12:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultas', '0002_delete_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centro_investigacion',
            fields=[
                ('codigo_Centro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('fecha_creacion_Centro', models.DateField()),
                ('grupo', models.CharField(max_length=50)),
                ('codigo_IES', models.CharField(max_length=50)),
                ('nombre_IES', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('idRol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('crear_Usuarios', models.CharField(max_length=100)),
                ('registrar_Informacion', models.CharField(max_length=100)),
                ('modificar_Informacion', models.CharField(max_length=100)),
                ('eliminar_Informacion', models.CharField(max_length=100)),
                ('crear_Proyecto', models.CharField(max_length=100)),
                ('realizar_Consulta_filtrada', models.CharField(max_length=100)),
                ('adjuntar_archivos', models.CharField(max_length=100)),
                ('enviar_informes', models.CharField(max_length=100)),
                ('asignar_proyecto', models.CharField(max_length=100)),
                ('publicar_Noticias', models.CharField(max_length=100)),
                ('descargar_archivos', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('mail_institucional', models.CharField(max_length=100)),
                ('facultad', models.CharField(max_length=100)),
                ('nro_Proyectos_a_Cargo', models.IntegerField()),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Roles')),
            ],
        ),
        migrations.AddField(
            model_name='centro_investigacion',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Usuarios'),
        ),
    ]
