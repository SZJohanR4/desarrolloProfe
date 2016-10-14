# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Actividades(models.Model):
    idactividad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fecha_limite = models.DateField()
    nota = models.IntegerField()
    adjunto = models.CharField(max_length=100)
    fk_director = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='fk_director')
    fk_estudiante = models.ForeignKey('Estudiante', models.DO_NOTHING, db_column='fk_estudiante')
    fk_proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='fk_proyecto')

    class Meta:
        managed = False
        db_table = 'actividades'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Ciclo(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ciclo'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estudiante(models.Model):
    idestudiante = models.AutoField(primary_key=True)
    sede = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=100)
    documento = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    programa_consequitivo = models.CharField(max_length=100)
    cod_programa = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    otro_telefono = models.CharField(max_length=100)
    celular = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    mail_institucional = models.CharField(max_length=100)
    investigacion = models.CharField(max_length=100)
    nombre_investigacion = models.CharField(max_length=100)
    nota = models.IntegerField()
    password = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    rol_segun_colciencias = models.CharField(max_length=100)
    nombre_materia_programa_estudiante = models.CharField(max_length=100)
    codigo_materia_programa_estudiante = models.CharField(max_length=100)
    opcion_proyecto1 = models.CharField(max_length=100)
    opcion_proyecto2 = models.CharField(max_length=100)
    opcion_proyecto3 = models.CharField(max_length=100)
    fecha_postulacion = models.DateField()
    fk_facultad = models.ForeignKey('Facultad', models.DO_NOTHING, db_column='fk_facultad')
    fk_ciclo = models.ForeignKey(Ciclo, models.DO_NOTHING, db_column='fk_ciclo')
    fk_programa = models.ForeignKey('Programa', models.DO_NOTHING, db_column='fk_programa')
    fk_proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='fk_proyecto')

    class Meta:
        managed = False
        db_table = 'estudiante'


class Facultad(models.Model):
    idfacultad = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fk_sede = models.ForeignKey('Sede', models.DO_NOTHING, db_column='fk_sede')

    class Meta:
        managed = False
        db_table = 'facultad'


class FuentesDeFinanciacion(models.Model):
    idfuente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipofinanciacion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    valor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fuentes_de_financiacion'


class GruposDeInvestigacion(models.Model):
    codigo_grupo = models.AutoField(primary_key=True)
    nombre_ies = models.CharField(max_length=100)
    codigo_ies = models.CharField(max_length=100)
    nombre_grupo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_vigencia_grupo = models.DateField()

    class Meta:
        managed = False
        db_table = 'grupos_de_investigacion'


class LineasInvestigacion(models.Model):
    idlinea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    inscritos = models.CharField(max_length=100)
    finalizados = models.CharField(max_length=100)
    aprobaron = models.CharField(max_length=100)
    cancelaron = models.CharField(max_length=100)
    perdieron = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'lineas_investigacion'


class MaximosNivelEducativo(models.Model):
    codigo = models.AutoField(primary_key=True)
    nivel = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'maximos_nivel_educativo'


class Noticias(models.Model):
    idnoticia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    fk_idpropietario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='fk_idpropietario')

    class Meta:
        managed = False
        db_table = 'noticias'


class NucleoBasicoConocimiento(models.Model):
    codigo = models.AutoField(primary_key=True)
    area = models.CharField(max_length=100)
    nbc = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'nucleo_basico_conocimiento'


class ProductosDeInvestigacion(models.Model):
    codigo_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    ano_obtencion_producto = models.CharField(max_length=100)
    mes_obtencion_producto = models.CharField(max_length=100)
    costo_producto = models.CharField(max_length=100)
    codigo_ies = models.CharField(max_length=100)
    nombre_ies = models.CharField(max_length=100)
    fk_proyecto = models.ForeignKey('Proyecto', models.DO_NOTHING, db_column='fk_proyecto')

    class Meta:
        managed = False
        db_table = 'productos_de_investigacion'


class Programa(models.Model):
    idprograma = models.AutoField(primary_key=True)
    codigo_programa = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    fk_facultad = models.ForeignKey(Facultad, models.DO_NOTHING, db_column='fk_facultad')

    class Meta:
        managed = False
        db_table = 'programa'


class Proyecto(models.Model):
    codigo_proyecto = models.AutoField(primary_key=True)
    codigo_ies = models.CharField(max_length=100)
    nombre_macroproyecto = models.CharField(max_length=100)
    nombre_ies = models.CharField(max_length=100)
    ano = models.CharField(max_length=100)
    semetre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    diracion = models.CharField(max_length=100)
    objetivo_socioeconomico = models.TextField()
    objetivo_proyecto = models.TextField()
    resumen_proyecto = models.TextField()
    resultados_esperados = models.TextField()
    sede = models.CharField(max_length=100)
    nombre_materia = models.CharField(max_length=100)
    codigo_materia = models.CharField(max_length=100)
    grupo_materia = models.CharField(max_length=100)
    horas_asignadas = models.CharField(max_length=100)
    gasto_total = models.FloatField()
    tipo_de_gasto = models.CharField(max_length=100)
    valor_semana = models.CharField(max_length=100)
    sublinea = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    nombre_jurados = models.CharField(max_length=100)
    perfiles = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    realizo_sustentacion_publica = models.CharField(max_length=100)
    otras_entidades_participantes = models.CharField(max_length=100)
    asociado_al_area_de_conocimiento = models.CharField(max_length=100)
    finalizado = models.CharField(max_length=100)
    paz_y_salvo = models.CharField(max_length=100)
    modalidad_de_seminario = models.CharField(max_length=100)
    fk_tipo_proyecto = models.ForeignKey('TiposProyecto', models.DO_NOTHING, db_column='fk_tipo_proyecto')
    fk_idgrupo_investigacion = models.ForeignKey(GruposDeInvestigacion, models.DO_NOTHING, db_column='fk_idgrupo_investigacion')
    fk_idlineas_investigacion = models.ForeignKey(LineasInvestigacion, models.DO_NOTHING, db_column='fk_idlineas_investigacion')
    fk_tipo_participacion_proyecto = models.ForeignKey('TipoParticipacionProyecto', models.DO_NOTHING, db_column='fk_tipo_participacion_proyecto')
    fk_nbc = models.ForeignKey(NucleoBasicoConocimiento, models.DO_NOTHING, db_column='fk_nbc')
    fk_maximo_nivel_educativo = models.ForeignKey(MaximosNivelEducativo, models.DO_NOTHING, db_column='fk_maximo_nivel_educativo')
    fk_fuente_de_financiacion = models.ForeignKey(FuentesDeFinanciacion, models.DO_NOTHING, db_column='fk_fuente_de_financiacion')
    fk_director_proyecto = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='fk_director_proyecto')
    fk_red_cooperacion = models.ForeignKey('RedesDeCoperacion', models.DO_NOTHING, db_column='fk_red_cooperacion')

    class Meta:
        managed = False
        db_table = 'proyecto'


class RedesDeCoperacion(models.Model):
    codigo_red = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    codigo_ies = models.CharField(max_length=100)
    nombre_ies = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    sector = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'redes_de_coperacion'


class Sede(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sede'


class TipoParticipacionProyecto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_participacion_proyecto'


class TiposProyecto(models.Model):
    codigo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipos_proyecto'
