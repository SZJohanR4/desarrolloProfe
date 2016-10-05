from django.db import models

# Create your models here.
class Roles(models.Model):
    nombre= models.CharField(max_length=100)
    crear_Usuario=models.CharField(max_length=100)
    registrar_Informacion=models.CharField(max_length=100)
    modificar_Informacion=models.CharField(max_length=100)
    eliminar_Informacion=models.CharField(max_length=100)
    crear_Proyecto=models.CharField(max_length=100)
    realizar_Consulta_filtrada=models.CharField(max_length=100)
    cambiar_archivos=models.CharField(max_length=100)
    enviar_informes=models.CharField(max_length=100)
    asignar_proyecto=models.CharField(max_length=100)
    
    
    
class Usuarios(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    documento=models.IntegerField()
    telefono=models.IntegerField()
    celular=models.IntegerField()
    mail=models.EmailField()
    mail_institucional=models.EmailField()
    facultad=models.CharField(max_length=100)
    nro_Proyectos_a_cargo=models.IntegerField()
    
    rol=models.ForeignKey(Roles,on_delete=models.CASCADE)
    
    
class Centro_investigacion(models.Model):
    #codigo_Centro es igual al id que pone por defecto el django
    nombre=models.CharField(max_length=100)
    departamento=models.CharField(max_length=100)
    municipio=models.CharField(max_length=100)
    fecha_creacion_Centro=models.DateField()
    grupo=models.CharField(max_length=100)
    codigo_IES=models.CharField(max_length=100)
    nombre_IES=models.CharField(max_length=100)
    
    
    
# centro ppor grupo tabla de ManyToManyDescriptor

class Grupos_De_Investigacion(models.Model):
    #codigo grupo es el mismo id que pone django
    codigo_IES=models.CharField(max_length=100)
    nombre_IES=models.CharField(max_length=100)
    NBC=models.CharField(max_length=100)
    fecha_inicio_grupo=models.DateField()
    fecha_vigencia_grupo=models.DateField()
    investigadores_Internos=models.CharField(max_length=100)
    investigadores_externos=models.CharField(max_length=100)
    
    