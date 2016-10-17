from django.db import models

# Create your models here.
# Create your models here.

    
class Usuario(models.Model):
    usuario=models.CharField(max_length=50, primary_key=True)
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    documento=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100, blank= True, null = True)
    celular=models.CharField(max_length=100)
    mail=models.CharField(max_length=100)
    mail_institucional=models.CharField(max_length=100)
    facultad=models.CharField(max_length=100)
    nro_Proyectos_a_Cargo=models.IntegerField()
    rol=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    
class Noticia(models.Model):
    titulo=models.CharField(max_length=100)
    contenido=models.CharField(max_length=100)
    fecha_Publicacion=models.DateField()
    idPropietario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
    
    
    
class Grupo_De_Investigacion(models.Model):
    codigo_IES=models.CharField(max_length=50)
    nombre_IES=models.CharField(max_length=100)
    nombre_grupo=models.CharField(max_length=100)
    fecha_inicio_grupo=models.DateField()
    fecha_vigencia_grupo=models.DateField()
    
    def __str__(self):
        return self.codigo_IES
    
    
    
class Linea_Investigacion(models.Model):
    nombre=models.CharField(max_length=100)
    inscritos=models.CharField(max_length=100)
    finalizados=models.CharField(max_length=100)
    aprobaron=models.CharField(max_length=100)
    cancelaron=models.CharField(max_length=100)
    perdieron=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    


class Fuente_de_Financiacion(models.Model):
    nombre=models.CharField(max_length=100)
    tipoFinanciacion=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    sector=models.CharField(max_length=100)
    pais=models.CharField(max_length=100)
    valor=models.FloatField()
    
    def __str__(self):
        return self.nombre
    

class Tipo_Proyecto(models.Model):
    descripcion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.descripcion
    
    

class Maximo_Nivel_Educativo(models.Model):
    nivel=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nivel
    
    
    
class tipo_Participacion_Proyecto(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    

class Sede(models.Model):
    descripcion=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    
    def __str__(self):
        return self.descripcion
    


class Facultad(models.Model):
    nombre_Facultad=models.CharField(max_length=100)
    Descripcion=models.CharField(max_length=100)
    
    idSede=models.ForeignKey(Sede,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_Facultad
    
    
class Ciclo(models.Model):
    descripcion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.descripcion


class Programa(models.Model):
    codigo_programa=models.CharField(max_length=100)
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    
    idFacultad=models.ForeignKey(Facultad,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.codigo_programa
    
    
    
    
class Red_de_Coperacion(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    codigo_IES=models.CharField(max_length=100)
    nombre_IES=models.CharField(max_length=100)
    fecha_Creacion_Red=models.DateField()
    sector=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    

class Nucleo_Basico_Conocimiento(models.Model):
    area=models.CharField(max_length=100)
    nbc=models.CharField(max_length=100)

    def __str__(self):
        return self.area
    
    

class Proyecto(models.Model):
    codigo_IES=models.CharField(max_length=100)
    nombreMacroProyecto=models.CharField(max_length=100)
    nombre_IES=models.CharField(max_length=100)
    ano=models.CharField(max_length=50)
    semestre=models.CharField(max_length=50)
    titulo=models.CharField(max_length=100)
    fecha_inicio=models.DateField()
    duracion=models.CharField(max_length=50)
    objetivo_socioeconomico=models.TextField()
    objetivo_proyecto=models.TextField()
    resumen_proyecto=models.TextField()
    resultados_esperados=models.TextField()
    sede=models.CharField(max_length=50)
    nombre_materia=models.CharField(max_length=50)
    codigo_materia=models.CharField(max_length=50)
    grupo_materia=models.CharField(max_length=50)
    horas_asignadas_docente=models.IntegerField()
    gasto_total=models.FloatField()
    tipo_De_gasto=models.CharField(max_length=100)
    valor_semana=models.FloatField()
    sublinea=models.CharField(max_length=100)
    empresa=models.CharField(max_length=100)
    nombreJurados=models.CharField(max_length=100)
    perfiles=models.CharField(max_length=100)
    valor=models.CharField(max_length=50)
    realizo_Sustentacion_publica=models.CharField(max_length=50)
    otras_Entidades_Participantes=models.CharField(max_length=50)
    asociado_al_area_de_conocimiento=models.CharField(max_length=50)
    finalizado=models.CharField(max_length=50)
    paz_y_salvo=models.CharField(max_length=50)
    modalidad_de_seminario=models.CharField(max_length=50)
    
    
    
    tipo_proyecto=models.ForeignKey(Tipo_Proyecto,on_delete=models.CASCADE)
    idGrupo_investigacion=models.ForeignKey(Grupo_De_Investigacion,on_delete=models.CASCADE)
    id_lineas_investigacion_asociadas=models.ForeignKey(Linea_Investigacion,on_delete=models.CASCADE)
    tipo_participacion_proyecto=models.ForeignKey(tipo_Participacion_Proyecto,on_delete=models.CASCADE)
    NBC=models.ForeignKey(Nucleo_Basico_Conocimiento,on_delete=models.CASCADE)
    maximo_nivel_educativo=models.ForeignKey(Maximo_Nivel_Educativo,on_delete=models.CASCADE)
    Fuente_de_financiacion=models.ForeignKey(Fuente_de_Financiacion,on_delete=models.CASCADE)
    directorDeProyecto=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    red_investigacion=models.ForeignKey(Red_de_Coperacion,on_delete=models.CASCADE)


    def __str__(self):
        return self.codigo_IES
    
    
    
class Estudiante(models.Model):
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
    rol=models.CharField(max_length=100)
    rol_Segun_Colciencias=models.CharField(max_length=100)
    nombreMateriaProgramaEstudiante=models.CharField(max_length=100)
    codigoMateriaProgramaEstudiante=models.CharField(max_length=100)
    opcionProyecto1=models.CharField(max_length=100)
    opcionProyecto2=models.CharField(max_length=100)
    opcionProyecto3=models.CharField(max_length=100)
    fecha_Postulacion=models.DateField()
    
    facultad=models.ForeignKey(Facultad,on_delete=models.CASCADE)
    ciclo=models.ForeignKey(Ciclo,on_delete=models.CASCADE)
    programa=models.ForeignKey(Programa,on_delete=models.CASCADE)
    proyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return self.sede
    
    
    
    
class Producto_de_Investigacion(models.Model):
    nombre=models.CharField(max_length=100)
    tipo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    ano_obtencion_producto=models.CharField(max_length=100)
    mes_obtencion_producto=models.CharField(max_length=100)
    costo_producto=models.FloatField()
    codigo_IES=models.CharField(max_length=100)
    nombre_IES=models.CharField(max_length=100)
    
    idProyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    

class Actividad(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    fecha_Limite=models.DateField()
    
    idDirector=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    idProyecto=models.ForeignKey(Proyecto,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class Actividad_Estudiante(models.Model):
    nota=models.IntegerField(blank=True, null=True)
    desarrollo=models.CharField(max_length=100, blank=True, null=True)
    adjunto=models.CharField(max_length=100, blank=True, null=True)

    idActividad=models.ForeignKey(Actividad, on_delete=models.CASCADE)
    idEstudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE)
