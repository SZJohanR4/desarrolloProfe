from django.db import models

# Create your models here.
class Roles(models.Model):
    idRol=models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=100)
    crear_Usuarios=models.CharField(max_length=100)
    registrar_Informacion=models.CharField(max_length=100)
    modificar_Informacion=models.CharField(max_length=100)
    eliminar_Informacion=models.CharField(max_length=100)
    crear_Proyecto=models.CharField(max_length=100)
    realizar_Consulta_filtrada=models.CharField(max_length=100)
    adjuntar_archivos=models.CharField(max_length=100)
    enviar_informes=models.CharField(max_length=100)
    asignar_proyecto=models.CharField(max_length=100)
    publicar_Noticias=models.CharField(max_length=100)
    descargar_archivos=models.CharField(max_length=100)
    
    
    
class Usuarios(models.Model):
    idUsuario=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    documento=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    celular=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    mail_institucional=models.CharField(max_length=100)
    facultad=models.CharField(max_length=100)
    nro_Proyectos_a_Cargo=models.IntegerField()
    
    rol=models.ForeignKey(Roles,on_delete=models.CASCADE)
    
class Grupos_De_Investigacion(models.Model):
    codigo_grupo=models.AutoField(primary_key=True)
    codigo_IES=models.CharField(max_length=50)
    nombre_IES=models.CharField(max_length=100)
    nombre_grupo=models.CharField(max_length=100)
    fecha_inicio_grupo=models.DateField()
    fecha_vigencia_grupo=models.DateField()
    
    
    
    
class Centro_investigacion(models.Model):
    codigo_Centro=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    departamento=models.CharField(max_length=50)
    municipio=models.CharField(max_length=50)
    fecha_creacion_Centro=models.DateField()
    codigo_IES=models.CharField(max_length=50)
    nombre_IES=models.CharField(max_length=100)
    
    idUsuario=models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    centro_Por_Grupo=models.ManyToManyField(Grupos_De_Investigacion)

class Noticias(models.Model):
    idNoticia=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100)
    contenido=models.CharField(max_length=100)
    fecha_Publicacion=models.DateField()
    
    idPropietario=models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    

class Lineas_Investigacion(models.Model):
    idLinea=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    inscritos=models.CharField(max_length=100)
    finalizados=models.CharField(max_length=100)
    aprobaron=models.CharField(max_length=100)
    cancelaron=models.CharField(max_length=100)
    perdieron=models.CharField(max_length=100)
    


class Fuentes_de_Financiacion(models.Model):
    idFuente=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    tipoFinanciacion=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    sector=models.CharField(max_length=100)
    pais=models.CharField(max_length=100)
    valor=models.FloatField()
    
    
    

class Tipos_Proyectos(models.Model):
    codigo=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=100)



class Maximo_Nivel_Educativo(models.Model):
    codigo=models.AutoField(primary_key=True)
    Nivel=models.CharField(max_length=100)
    
class tipo_Participacion_Proyecto(models.Model):
    codigo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    
    




class Facultades(models.Model):
    idFacultad=models.AutoField(primary_key=True)
    nombre_Facultad=models.CharField(max_length=100)
    Descripcion=models.CharField(max_length=100)

class Ciclos(models.Model):
    codigo=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=100)


class Programas(models.Model):
    idPrograma=models.AutoField(primary_key=True)
    codigo_programa=models.CharField(max_length=100)
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    
    idFacultad=models.ForeignKey(Facultades,on_delete=models.CASCADE)






class Estudiantes(models.Model):
    idEstudiante=models.AutoField(primary_key=True)
    sede=models.CharField(max_length=100)
    tipo_documento=models.CharField(max_length=100)
    documento=models.CharField(max_length=100)
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    programa_Consecutivo=models.CharField(max_length=100)
    cod_Programa=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    otro_Telefono=models.CharField(max_length=100)
    celular=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    mail_institucional=models.CharField(max_length=100)
    investigacion=models.CharField(max_length=50)
    nombre_Investigacion_Trabajo_grado=models.CharField(max_length=100)
    nota=models.IntegerField()
    password=models.CharField(max_length=100)
    
    facultad=models.ForeignKey(Facultades,on_delete=models.CASCADE)
    ciclo=models.ForeignKey(Ciclos,on_delete=models.CASCADE)
    programa=models.ForeignKey(Programas,on_delete=models.CASCADE)
    
    Estudiante_Por_Grupo=models.ManyToManyField(Grupos_De_Investigacion)


class Sedes(models.Model):
    codigo=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    
    Sedes_Por_Facultad=models.ManyToManyField(Facultades)

class Proyectos(models.Model):
    codigo_IES=models.AutoField(primary_key=True)
    nombre_IES=models.CharField(max_length=100)
    año=models.CharField(max_length=50)
    semestre=models.CharField(max_length=50)
    titulo=models.CharField(max_length=100)
    fecha_inicio=models.DateField()
    duracion=models.CharField(max_length=50)
    objetivo_socioeconomico=models.TextField()
    objetivo_proyecto=models.TextField()
    resumen_proyecto=models.TextField()
    resultados_esperados=models.TextField()
    nombre_materia=models.CharField(max_length=50)
    codigo_materia=models.CharField(max_length=50)
    grupo_materia=models.CharField(max_length=50)
    nombre_programa_de_materia_estudiante=models.CharField(max_length=50)
    codigo_programa_de_materia_estudiante=models.CharField(max_length=50)
    programa_estudiante=models.CharField(max_length=50)
    codigo_programa_estudiante=models.CharField(max_length=50)
    tipo_identificacion=models.CharField(max_length=50)
    nro_identificacion=models.CharField(max_length=100)
    nombres=models.CharField(max_length=100)
    rol=models.CharField(max_length=50)
    rol_Segun_Colciencias=models.CharField(max_length=50)
    NBC=models.CharField(max_length=50)
    horas_asignadas_docente=models.IntegerField()
    gasto_total=models.FloatField()
    tipo_De_gasto=models.CharField(max_length=100)
    valor_semana=models.FloatField()
    correo_electronico=models.CharField(max_length=100)
    
   
    tipo_proyecto=models.ForeignKey(Tipos_Proyectos,on_delete=models.CASCADE)
    idGrupo_investigacion=models.ForeignKey(Grupos_De_Investigacion,on_delete=models.CASCADE)
    tipo_participacion_proyecto=models.ForeignKey(tipo_Participacion_Proyecto,on_delete=models.CASCADE)
    maximo_nivel_educativo=models.ForeignKey(Maximo_Nivel_Educativo,on_delete=models.CASCADE)
    
    Linea_Por_Proyecto=models.ManyToManyField(Lineas_Investigacion)
    Centro_Por_Proyectos=models.ManyToManyField(Centro_investigacion)
    Fuente_Por_Proyecto=models.ManyToManyField(Fuentes_de_Financiacion)
    Proyecto_Por_Sede=models.ManyToManyField(Sedes)
    
    
    
class Productos_de_Investigacion(models.Model):
    codigo_producto=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    año_obtencion_producto=models.CharField(max_length=100)
    mes_obtencion_producto=models.CharField(max_length=100)
    costo_producto=models.FloatField()
    codigo_IES=models.CharField(max_length=100)
    nombre_IES=models.CharField(max_length=100)
    
    idProyecto=models.ForeignKey(Proyectos,on_delete=models.CASCADE)
    
    
class Nucleo_Basico_Conocimiento(models.Model):
    codigo=models.AutoField(primary_key=True)
    area=models.CharField(max_length=100)
    nbc=models.CharField(max_length=100)
    
    Productos_por_NBC=models.ManyToManyField(Productos_de_Investigacion)
    Grupos_Por_NBC=models.ManyToManyField(Grupos_De_Investigacion)
    
    
class Investigadores_De_IES(models.Model):
    idInvestigador=models.AutoField(primary_key=True)
    tipo_Identificacion=models.CharField(max_length=100)
    numero_identificacion=models.CharField(max_length=100)
    nombres=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    tipo_Participacion_proyecto=models.CharField(max_length=100)
    tipo_investigador=models.CharField(max_length=100)
    area=models.CharField(max_length=100)
    
    Investigadores_Por_NBC=models.ManyToManyField(Nucleo_Basico_Conocimiento)
    grupos_Por_Investigador=models.ManyToManyField(Grupos_De_Investigacion)
    Proyectos_Por_Investigador=models.ManyToManyField(Proyectos)
    
class Redes_de_Coperacion(models.Model):
    codigo_red=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    codigo_IES=models.CharField(max_length=100)
    nombre_IES=models.CharField(max_length=100)
    fecha_Creacion_Red=models.DateField()
    
    Proyectos_Por_Redes=models.ManyToManyField(Proyectos)


class Sector(models.Model):
    codigo=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=100)
    
    red_Por_sector=models.ManyToManyField(Redes_de_Coperacion)
    
    
class Integrantes_de_red(models.Model):
    idIntegrante=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    pais=models.CharField(max_length=100)
    fecha_vinculacion=models.DateField()
    fecha_retiro=models.DateField()
    tipo=models.CharField(max_length=100)
    IES=models.CharField(max_length=100)
    
    sector=models.ForeignKey(Sector,on_delete=models.CASCADE)
    idRed=models.ForeignKey(Redes_de_Coperacion,on_delete=models.CASCADE)