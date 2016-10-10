# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-10 17:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0004_auto_20161006_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centro_investigacion',
            name='centro_Por_Grupo',
        ),
        migrations.RemoveField(
            model_name='centro_investigacion',
            name='idUsuario',
        ),
        migrations.RemoveField(
            model_name='estudiantes',
            name='Estudiante_Por_Grupo',
        ),
        migrations.RemoveField(
            model_name='estudiantes',
            name='ciclo',
        ),
        migrations.RemoveField(
            model_name='estudiantes',
            name='facultad',
        ),
        migrations.RemoveField(
            model_name='estudiantes',
            name='programa',
        ),
        migrations.RemoveField(
            model_name='integrantes_de_red',
            name='idRed',
        ),
        migrations.RemoveField(
            model_name='integrantes_de_red',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='investigadores_de_ies',
            name='Investigadores_Por_NBC',
        ),
        migrations.RemoveField(
            model_name='investigadores_de_ies',
            name='Proyectos_Por_Investigador',
        ),
        migrations.RemoveField(
            model_name='investigadores_de_ies',
            name='grupos_Por_Investigador',
        ),
        migrations.RemoveField(
            model_name='noticias',
            name='idPropietario',
        ),
        migrations.RemoveField(
            model_name='nucleo_basico_conocimiento',
            name='Grupos_Por_NBC',
        ),
        migrations.RemoveField(
            model_name='nucleo_basico_conocimiento',
            name='Productos_por_NBC',
        ),
        migrations.RemoveField(
            model_name='productos_de_investigacion',
            name='idProyecto',
        ),
        migrations.RemoveField(
            model_name='programas',
            name='idFacultad',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='Centro_Por_Proyectos',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='Fuente_Por_Proyecto',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='Linea_Por_Proyecto',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='Proyecto_Por_Sede',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='idGrupo_investigacion',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='maximo_nivel_educativo',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='tipo_participacion_proyecto',
        ),
        migrations.RemoveField(
            model_name='proyectos',
            name='tipo_proyecto',
        ),
        migrations.RemoveField(
            model_name='redes_de_coperacion',
            name='Proyectos_Por_Redes',
        ),
        migrations.RemoveField(
            model_name='sector',
            name='red_Por_sector',
        ),
        migrations.RemoveField(
            model_name='sedes',
            name='Sedes_Por_Facultad',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='rol',
        ),
        migrations.DeleteModel(
            name='Centro_investigacion',
        ),
        migrations.DeleteModel(
            name='Ciclos',
        ),
        migrations.DeleteModel(
            name='Estudiantes',
        ),
        migrations.DeleteModel(
            name='Facultades',
        ),
        migrations.DeleteModel(
            name='Fuentes_de_Financiacion',
        ),
        migrations.DeleteModel(
            name='Grupos_De_Investigacion',
        ),
        migrations.DeleteModel(
            name='Integrantes_de_red',
        ),
        migrations.DeleteModel(
            name='Investigadores_De_IES',
        ),
        migrations.DeleteModel(
            name='Lineas_Investigacion',
        ),
        migrations.DeleteModel(
            name='Maximo_Nivel_Educativo',
        ),
        migrations.DeleteModel(
            name='Noticias',
        ),
        migrations.DeleteModel(
            name='Nucleo_Basico_Conocimiento',
        ),
        migrations.DeleteModel(
            name='Productos_de_Investigacion',
        ),
        migrations.DeleteModel(
            name='Programas',
        ),
        migrations.DeleteModel(
            name='Proyectos',
        ),
        migrations.DeleteModel(
            name='Redes_de_Coperacion',
        ),
        migrations.DeleteModel(
            name='Roles',
        ),
        migrations.DeleteModel(
            name='Sector',
        ),
        migrations.DeleteModel(
            name='Sedes',
        ),
        migrations.DeleteModel(
            name='tipo_Participacion_Proyecto',
        ),
        migrations.DeleteModel(
            name='Tipos_Proyectos',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
    ]
