# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-17 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('fecha_Limite', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Actividad_Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField(blank=True, null=True)),
                ('desarrollo', models.CharField(blank=True, max_length=100, null=True)),
                ('adjunto', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ciclo',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('usuario', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('tipo_documento', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=100)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('programa_Consecutivo', models.CharField(blank=True, max_length=100, null=True)),
                ('cod_Programa', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(max_length=100)),
                ('otro_Telefono', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('mail_institucional', models.CharField(max_length=100)),
                ('investigacion', models.CharField(max_length=50)),
                ('nombre_Investigacion_Trabajo_grado', models.CharField(blank=True, max_length=100, null=True)),
                ('nota', models.IntegerField(blank=True, null=True)),
                ('password', models.CharField(max_length=100)),
                ('rol', models.CharField(blank=True, max_length=100, null=True)),
                ('rol_Segun_Colciencias', models.CharField(blank=True, max_length=100, null=True)),
                ('nombreMateriaProgramaEstudiante', models.CharField(blank=True, max_length=100, null=True)),
                ('codigoMateriaProgramaEstudiante', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_Postulacion', models.DateField(blank=True, null=True)),
                ('ciclo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Ciclo')),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fuente_de_Financiacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipoFinanciacion', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('sector', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Grupo_De_Investigacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_IES', models.CharField(max_length=50)),
                ('nombre_IES', models.CharField(max_length=100)),
                ('nombre_grupo', models.CharField(max_length=100)),
                ('fecha_inicio_grupo', models.DateField()),
                ('fecha_vigencia_grupo', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Linea_Investigacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('inscritos', models.CharField(max_length=100)),
                ('finalizados', models.CharField(max_length=100)),
                ('aprobaron', models.CharField(max_length=100)),
                ('cancelaron', models.CharField(max_length=100)),
                ('perdieron', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Maximo_Nivel_Educativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.CharField(max_length=100)),
                ('fecha_Publicacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Nucleo_Basico_Conocimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=100)),
                ('nbc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto_de_Investigacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('ano_obtencion_producto', models.CharField(max_length=100)),
                ('mes_obtencion_producto', models.CharField(max_length=100)),
                ('costo_producto', models.FloatField()),
                ('codigo_IES', models.CharField(max_length=100)),
                ('nombre_IES', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_programa', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('idFacultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Facultad')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_IES', models.CharField(blank=True, max_length=100, null=True)),
                ('nombreMacroProyecto', models.CharField(max_length=100)),
                ('nombre_IES', models.CharField(max_length=100)),
                ('ano', models.CharField(blank=True, max_length=50, null=True)),
                ('semestre', models.CharField(blank=True, max_length=50, null=True)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('duracion', models.CharField(blank=True, max_length=50, null=True)),
                ('objetivo_socioeconomico', models.TextField(blank=True, null=True)),
                ('objetivo_proyecto', models.TextField()),
                ('resumen_proyecto', models.TextField(blank=True, null=True)),
                ('resultados_esperados', models.TextField(blank=True, null=True)),
                ('sede', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre_materia', models.CharField(blank=True, max_length=50, null=True)),
                ('codigo_materia', models.CharField(blank=True, max_length=50, null=True)),
                ('grupo_materia', models.CharField(blank=True, max_length=50, null=True)),
                ('horas_asignadas_docente', models.IntegerField(blank=True, null=True)),
                ('gasto_total', models.FloatField(blank=True, null=True)),
                ('tipo_De_gasto', models.CharField(blank=True, max_length=100, null=True)),
                ('valor_semana', models.FloatField(blank=True, null=True)),
                ('sublinea', models.CharField(max_length=100)),
                ('empresa', models.CharField(max_length=100)),
                ('nombreJurados', models.CharField(max_length=100)),
                ('perfiles', models.CharField(max_length=100)),
                ('valor', models.CharField(blank=True, max_length=50, null=True)),
                ('realizo_Sustentacion_publica', models.CharField(blank=True, max_length=50, null=True)),
                ('otras_Entidades_Participantes', models.CharField(blank=True, max_length=50, null=True)),
                ('asociado_al_area_de_conocimiento', models.CharField(blank=True, max_length=50, null=True)),
                ('finalizado', models.CharField(blank=True, max_length=50, null=True)),
                ('paz_y_salvo', models.CharField(blank=True, max_length=50, null=True)),
                ('modalidad_de_seminario', models.CharField(blank=True, max_length=50, null=True)),
                ('Fuente_de_financiacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultas.Fuente_de_Financiacion')),
                ('NBC', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultas.Nucleo_Basico_Conocimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Red_de_Coperacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('codigo_IES', models.CharField(max_length=100)),
                ('nombre_IES', models.CharField(max_length=100)),
                ('fecha_Creacion_Red', models.DateField()),
                ('sector', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_Participacion_Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Proyecto',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuario', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=100, null=True)),
                ('celular', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('mail_institucional', models.CharField(max_length=100)),
                ('facultad', models.CharField(max_length=100)),
                ('nro_Proyectos_a_Cargo', models.IntegerField(blank=True, null=True)),
                ('rol', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='proyecto',
            name='directorDeProyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Usuario'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='idGrupo_investigacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultas.Grupo_De_Investigacion'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='id_lineas_investigacion_asociadas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultas.Linea_Investigacion'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='maximo_nivel_educativo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultas.Maximo_Nivel_Educativo'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='red_investigacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultas.Red_de_Coperacion'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='tipo_participacion_proyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consultas.tipo_Participacion_Proyecto'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='tipo_proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Tipo_Proyecto'),
        ),
        migrations.AddField(
            model_name='producto_de_investigacion',
            name='idProyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Proyecto'),
        ),
        migrations.AddField(
            model_name='noticia',
            name='idPropietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Usuario'),
        ),
        migrations.AddField(
            model_name='facultad',
            name='idSede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Sede'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='facultad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Facultad'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Programa'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Proyecto'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='sede',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Sede'),
        ),
        migrations.AddField(
            model_name='actividad_estudiante',
            name='UsuarioEstudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Estudiante'),
        ),
        migrations.AddField(
            model_name='actividad_estudiante',
            name='idActividad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Actividad'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='idDirector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Usuario'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='idProyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultas.Proyecto'),
        ),
    ]
