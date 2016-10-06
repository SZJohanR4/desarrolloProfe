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
    
    def __str__(self):
        return self.nombre
    
    def insert(nombre_r,crear_Usuario_r,registrar_Informacion_r,modificar_Informacion_r
               ,eliminar_Informacion_r,crear_Proyecto_r,realizar_Consulta_filtrada_r
               ,adjuntar_archivos_r,enviar_informes_r,asignar_proyecto_r,publicar_Noticias_r,descargar_archivos_r):
        r=Roles()
        r.nombre=nombre_r
        r.crear_Usuario=crear_Usuario_r
        r.registrar_Informacion=registrar_Informacion_r
        r.modificar_Informacion=modificar_Informacion_r
        r.eliminar_Informacion=eliminar_Informacion_r
        r.crear_Proyecto=crear_Proyecto_r
        r.realizar_Consulta_filtrada=realizar_Consulta_filtrada_r
        r.adjuntar_archivos=adjuntar_archivos_r
        r.enviar_informes=enviar_informes_r
        r.asignar_proyecto=asignar_proyecto_r
        r.publicar_Noticias=publicar_Noticias_r
        r.descargar_archivos=descargar_archivos_r
     
        r.save()
        return "Ha insertado el Rol: "+nombre+" exitosamente."
    
    def update(id_acualizar_r,nombre_r,crear_Usuario_r,registrar_Informacion_r,modificar_Informacion_r
               ,eliminar_Informacion_r,crear_Proyecto_r,realizar_Consulta_filtrada_r
               ,adjuntar_archivos_r,enviar_informes_r,asignar_proyecto_r,publicar_Noticias_r,descargar_archivos_r):
        r=Roles()
        r.id=id_actualizar_r
        r.nombre=nombre_r
        r.crear_Usuario=crear_Usuario_r
        r.registrar_Informacion=registrar_Informacion_r
        r.modificar_Informacion=modificar_Informacion_r
        r.eliminar_Informacion=eliminar_Informacion_r
        r.crear_Proyecto=crear_Proyecto_r
        r.realizar_Consulta_filtrada=realizar_Consulta_filtrada_r
        r.adjuntar_archivos=adjuntar_archivos_r
        r.enviar_informes=enviar_informes_r
        r.asignar_proyecto=asignar_proyecto_r
        r.publicar_Noticias=publicar_Noticias_r
        r.descargar_archivos=descargar_archivos_r
        r.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_r):
        return Roles.objects.filter(id=id_r).values('id','nombre','crear_Usuario','registrar_Informacion',
                                                    'modificar_Informacion','eliminar_Informacion','crear_Proyecto',
                                                    'realizar_Consulta_filtrada','adjuntar_archivos','enviar_informes'
                                                    ,'asignar_proyecto','publicar_Noticias','descargar_archivos')

    def delete(id_r):
        r=Roles.objects.filter(id=id_r)
        r.delete()
        
        return "Ha borrado a: "+ id_r
    
    
    
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
    
    def __str__(self):
        return self.nombre
    
    def insert(nombre_u,apellido_u,password_u,documento_u
               ,telefono_u,celular_u,mail_u
               ,mail_institucional_u,facultad_u,nro_Proyectos_a_cargo_u,rol_u):
        U=Usuarios()
        U.nombre=nombre_u
        U.apellido=apellido_u
        U.password=password_u
        U.documento=documento_u
        U.telefono=telefono_u
        U.celular=celular_u
        U.mail=mail_u
        U.mail_institucional=mail_institucional_u
        U.facultad=facultad_u
        U.nro_Proyectos_a_cargo=nro_Proyectos_a_cargo_u
        U.rol=rol_u
     
        U.save()
        return "Ha insertado el Usuario: "+nombre+" exitosamente."
    
    def update(id_acualizar_u,nombre_u,apellido_u,password_u,documento_u
               ,telefono_u,celular_u,mail_u
               ,mail_institucional_u,facultad_u,nro_Proyectos_a_cargo_u,rol_u):
        U=Usuarios()
        U.id=id_actualizar_u
        U.nombre=nombre_u
        U.apellido=apellido_u
        U.password=password_u
        U.documento=documento_u
        U.telefono=telefono_u
        U.celular=celular_u
        U.mail=mail_u
        U.mail_institucional=mail_institucional_u
        U.facultad=facultad_u
        U.nro_Proyectos_a_cargo=nro_Proyectos_a_cargo_u
        U.rol=rol_u
        U.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_u):
        return Roles.objects.filter(id=id_u).values('id','nombre','apellido','password',
                                                    'documento','telefono','celular',
                                                    'mail','mail_institucional','facultad'
                                                    ,'nro_Proyectos_a_cargo','rol')

    def delete(id_u):
        U=Roles.objects.filter(id=id_u)
        U.delete()
        
        return "Ha borrado a: "+ id_u
    
class Grupos_De_Investigacion(models.Model):
    codigo_grupo=models.AutoField(primary_key=True)
    codigo_IES=models.CharField(max_length=50)
    nombre_IES=models.CharField(max_length=100)
    nombre_grupo=models.CharField(max_length=100)
    fecha_inicio_grupo=models.DateField()
    fecha_vigencia_grupo=models.DateField()
    
    def __str__(self):
        return self.codigo_grupo
    
    def insert(codigo_grupo_GDI,codigo_IES_GDI,nombre_IES_GDI,nombre_grupo_GDI
               ,fecha_inicio_grupo_GDI,fecha_vigencia_grupo_GDI):
        GDI=Grupos_De_Investigacion()
        GDI.codigo_grupo=codigo_grupo_GDI
        GDI.codigo_IES=codigo_IES_GDI
        GDI.nombre_IES=nombre_IES_GDI
        GDI.nombre_grupo=nombre_grupo_GDI
        GDI.fecha_inicio_grupo=fecha_inicio_grupo_GDI
        GDI.fecha_vigencia_grupo=fecha_vigencia_grupo_GDI
       
     
        GDI.save()
        return "Ha insertado el GRUPO DE INVESTIGACION: "+codigo_grupo_GDI+" exitosamente."
    
    def update(id_acualizar_GDI,codigo_grupo_GDI,codigo_IES_GDI,nombre_IES_GDI,nombre_grupo_GDI
               ,fecha_inicio_grupo_GDI,fecha_vigencia_grupo_GDI):
        
        
        GDI=Grupos_De_Investigacion()
        GDI.id=id_actualizar_GDI
        GDI.codigo_grupo=codigo_grupo_GDI
        GDI.codigo_IES=codigo_IES_GDI
        GDI.nombre_IES=nombre_IES_GDI
        GDI.nombre_grupo=nombre_grupo_GDI
        GDI.fecha_inicio_grupo=fecha_inicio_grupo_GDI
        GDI.fecha_vigencia_grupo=fecha_vigencia_grupo_GDI
        
        GDI.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_GDI):
        return Roles.objects.filter(id=id_r).values('id','codigo_grupo','codigo_IES','nombre_IES',
                                                    'nombre_grupo','fecha_inicio_grupo','fecha_vigencia_grupo')

    def delete(id_GDI):
        GDI=Roles.objects.filter(id=id_GDI)
        GDI.delete()
        
        return "Ha borrado a: "+ id_GDI
    
    
    
    
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
    
    def __str__(self):
        return self.nombre
    
    def insert(nombre_CI,departamento_CI,municipio_CI,fecha_creacion_Centro_CI
               ,grupo_CI,codigo_IES_CI,nombre_IES_CI
               ,idUsuario_CI):
        CI=Centro_investigacion()
        CI.nombre=nombre_CI
        CI.departamento=departamento_CI
        CI.municipio=municipio_CI
        CI.fecha_creacion_Centro=fecha_creacion_Centro_CI
        CI.grupo=grupo_CI
        CI.codigo_IES=codigo_IES_CI
        CI.nombre_IES=nombre_IES_CI
        CI.idUsuario=idUsuario_CI
     
        CI.save()
        return "Ha insertado el Centro de investigacion: "+nombre+" exitosamente."
    
    def update(id_acualizar_CI,nombre_CI,departamento_CI,municipio_CI,fecha_creacion_Centro_CI
               ,grupo_CI,codigo_IES_CI,nombre_IES_CI
               ,idUsuario_CI):
       
        
        CI=Centro_investigacion()
        CI.id=id_actualizar_CI
        CI.nombre=nombre_CI
        CI.departamento=departamento_CI
        CI.municipio=municipio_CI
        CI.fecha_creacion_Centro=fecha_creacion_Centro_CI
        CI.grupo=grupo_CI
        CI.codigo_IES=codigo_IES_CI
        CI.nombre_IES=nombre_IES_CI
        CI.idUsuario=idUsuario_CI
        CI.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_CI):
        return Roles.objects.filter(id=id_CI).values('id','nombre','departamento','municipio',
                                                    'fecha_creacion_Centro','grupo','codigo_IES',
                                                    'nombre_IES','idUsuario')

    def delete(id_CI):
        CI=Roles.objects.filter(id=id_CI)
        CI.delete()
        
        return "Ha borrado a: "+ id_CI

class Noticias(models.Model):
    idNoticia=models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=100)
    contenido=models.CharField(max_length=100)
    fecha_Publicacion=models.DateField()
    
    idPropietario=models.ForeignKey(Usuarios,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
    
    def insert(titulo_N,contenido_N,fecha_Publicacion_N,idPropietario_N):
        N=Noticias()
        N.titulo=titulo_N
        N.contenido=contenido_N
        N.fecha_Publicacion=fecha_Publicacion_N
        N.idPropietario=idPropietario_N
     
        N.save()
        return "Ha insertado la Noticia: "+titulo+" exitosamente."
    
    def update(id_acualizar_N,titulo_N,contenido_N,fecha_Publicacion_N,idPropietario_N):
       
    
        N=Noticias()
        N.id=id_actualizar_N
        N.titulo=titulo_N
        N.contenido=contenido_N
        N.fecha_Publicacion=fecha_Publicacion_N
        N.idPropietario=idPropietario_N
        N.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_N):
        return Roles.objects.filter(id=id_N).values('id','titulo','contenido','fecha_Publicacion',
                                                    'idPropietario')

    def delete(id_N):
        N=Roles.objects.filter(id=id_N)
        N.delete()
        
        return "Ha borrado a: "+ id_N
    

class Lineas_Investigacion(models.Model):
    idLinea=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    inscritos=models.CharField(max_length=100)
    finalizados=models.CharField(max_length=100)
    aprobaron=models.CharField(max_length=100)
    cancelaron=models.CharField(max_length=100)
    perdieron=models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
    def insert(idLinea_LI,nombre_LI,inscritos_LI,finalizados_LI,aprobaron_LI
               ,cancelaron_LI,perdieron_LI):
        LI=Lineas_Investigacion()
        LI.idLinea=idLinea_LI
        LI.nombre=nombre_LI
        LI.inscritos=inscritos_LI
        LI.finalizados=finalizados_LI
        LI.aprobaron=aprobaron_LI
        LI.cancelaron=cancelaron_LI
        LI.perdieron=perdieron_LI
       
     
        LI.save()
        return "Ha insertado el GRUPO DE INVESTIGACION: "+codigo_grupo_GDI+" exitosamente."
    
    def update(idLinea_LI,nombre_LI,inscritos_LI,finalizados_LI,aprobaron_LI
               ,cancelaron_LI,perdieron_LI):
        
        
        LI=Lineas_Investigacion()
        LI.idLinea=idLinea_LI
        LI.nombre=nombre_LI
        LI.inscritos=inscritos_LI
        LI.finalizados=finalizados_LI
        LI.aprobaron=aprobaron_LI
        LI.cancelaron=cancelaron_LI
        LI.perdieron=perdieron_LI
        
        LI.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_LI):
        return Roles.objects.filter(idLinea=id_LI).values('idLinea','nombre','inscritos','finalizados',
                                                    'aprobaron','cancelaron','perdieron')

    def delete(id_LI):
        LI=Roles.objects.filter(idLinea=id_LI)
        LI.delete()
        
        return "Ha borrado a: "+ id_LI
    
    


class Fuentes_de_Financiacion(models.Model):
    idFuente=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    tipoFinanciacion=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    sector=models.CharField(max_length=100)
    pais=models.CharField(max_length=100)
    valor=models.FloatField()
    
    def __str__(self):
        return self.nombre
    
    def insert(idFuente_FF,nombre_FF,tipoFinanciacion_FF,descripcion_FF,sector_FF
               ,pais_FF,valor_FF):
        FF=Fuentes_de_Financiacion()
        FF.idFuente=idFuente_FF
        FF.nombre=nombre_FF
        FF.tipoFinanciacion=tipoFinanciacion_FF
        FF.descripcion=descripcion_FF
        FF.sector=sector_FF
        FF.pais=pais_FF
        FF.valor=valor_FF
       
     
        FF.save()
        return "Ha insertado FUENTE DE FINANCIACION: "+idFuente_FF+" exitosamente."
    
    def update(idFuente_FF,nombre_FF,tipoFinanciacion_FF,descripcion_FF,sector_FF
               ,pais_FF,valor_FF):
        
        
        FF=Fuentes_de_Financiacion()
        FF.idFuente=idFuente_FF
        FF.nombre=nombre_FF
        FF.tipoFinanciacion=tipoFinanciacion_FF
        FF.descripcion=descripcion_FF
        FF.sector=sector_FF
        FF.pais=pais_FF
        FF.valor=valor_FF
        
        FF.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_FF):
        return Roles.objects.filter(idFuente=id_FF).values('idFuente','nombre','tipoFinanciacion'
                                                           ,'descripcion',
                                                    'sector','pais','valor')

    def delete(id_FF):
        FF=Roles.objects.filter(idFuente=id_FF)
        FF.delete()
        
        return "Ha borrado a: "+ id_FF
    
    
    

class Tipos_Proyectos(models.Model):
    codigo=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.codigo
    
    def insert(codigo_TP,descripcion_TP):
        TP=Tipos_Proyectos()
        TP.codigo=codigo_TP
        TP.descripcion=descripcion_TP
        
       
     
        TP.save()
        return "Ha insertado EL TIPO DE PROYECTO: "+codigo_TP+" exitosamente."
    
    def update(codigo_TP,descripcion_TP):
        
        
        TP=Tipos_Proyectos()
        TP.codigo=codigo_TP
        TP.descripcion=descripcion_TP
        
       
     
        TP.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_TP):
        return Roles.objects.filter(codigo=id_TP).values('codigo','descripcion')

    def delete(id_TP):
        TP=Roles.objects.filter(codigo=id_TP)
        TP.delete()
        
        return "Ha borrado a: "+ id_TP



class Maximo_Nivel_Educativo(models.Model):
    codigo=models.AutoField(primary_key=True)
    Nivel=models.CharField(max_length=100)
    
    def __str__(self):
        return self.codigo
    
    def insert(codigo_MNE,Nivel_MNE):
        MNE=Maximo_Nivel_Educativo()
        MNE.codigo=codigo_MNE
        MNE.Nivel=Nivel_MNE
        
       
     
        MNE.save()
        return "Ha insertado MAXIMO NIVEL EDUCATIVO: "+codigo_MNE+" exitosamente."
    
    def update(codigo_MNE,Nivel_MNE):
        
        
        MNE=Maximo_Nivel_Educativo()
        MNE.codigo=codigo_MNE
        MNE.Nivel=Nivel_MNE
        
       
     
        MNE.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_MNE):
        return Roles.objects.filter(codigo=id_MNE).values('codigo','Nivel')

    def delete(id_MNE):
        MNE=Roles.objects.filter(codigo=id_MNE)
        MNE.delete()
        
        return "Ha borrado a: "+ id_MNE
    
class tipo_Participacion_Proyecto(models.Model):
    codigo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.codigo
    
    def insert(codigo_TPP,nombre_TPP,descripcion_TPP):
        TPP=tipo_Participacion_Proyecto()
        TPP.codigo=codigo_TPP
        TPP.nombre=nombre_TPP
        TPP.descripcion=descripcion_TPP
        
       
     
        TPP.save()
        return "Ha insertado tipo Participacion Proyecto: "+codigo_TPP+" exitosamente."
    
    def update(codigo_TPP,nombre_TPP,descripcion_TPP):
        
        
        TPP=tipo_Participacion_Proyecto()
        TPP.codigo=codigo_TPP
        TPP.nombre=nombre_TPP
        TPP.descripcion=descripcion_TPP
        
       
     
        TPP.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_TPP):
        return Roles.objects.filter(codigo=id_TPP).values('codigo','nombre','descripcion')

    def delete(id_TPP):
        TPP=Roles.objects.filter(codigo=id_TPP)
        TPP.delete()
        
        return "Ha borrado a: "+ id_TPP




class Facultades(models.Model):
    idFacultad=models.AutoField(primary_key=True)
    nombre_Facultad=models.CharField(max_length=100)
    Descripcion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.idFacultad
    
    def insert(idFacultad_F,nombre_Facultad_F,Descripcion_F):
        F=Facultades()
        F.idFacultad=idFacultad_F
        F.nombre_Facultad=nombre_Facultad_F
        F.Descripcion=Descripcion_F
        
       
     
        F.save()
        return "Ha insertado FACULTAD: "+idFacultad+" exitosamente."
    
    def update(idFacultad_F,nombre_Facultad_F,Descripcion_F):
        F=Facultades()
        F.idFacultad=idFacultad_F
        F.nombre_Facultad=nombre_Facultad_F
        F.Descripcion=Descripcion_F
        
       
     
        F.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_F):
        return Roles.objects.filter(idFacultad=id_F).values('idFacultad','nombre_Facultad','Descripcion')

    def delete(id_F):
        F=Roles.objects.filter(idFacultad=id_F)
        F.delete()
        
        return "Ha borrado a: "+ id_F
    
class Ciclos(models.Model):
    codigo=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.codigo
    
    def insert(codigo_C,descripcion_C):
        C=Ciclos()
        C.codigo=codigo_C
        C.descripcion=descripcion_C
       
        
       
     
        C.save()
        return "Ha insertado CICLO: "+codigo_C+" exitosamente."
    
    def update(codigo_C,descripcion_C):
        C=Ciclos()
        C.codigo=codigo_C
        C.descripcion=descripcion_C
        
       
     
        F.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_C):
        return Roles.objects.filter(codigo=id_C).values('codigo','descripcion')

    def delete(id_C):
        C=Roles.objects.filter(codigo=id_C)
        C.delete()
        
        return "Ha borrado a: "+ id_C


class Programas(models.Model):
    idPrograma=models.AutoField(primary_key=True)
    codigo_programa=models.CharField(max_length=100)
    nombre=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    
    idFacultad=models.ForeignKey(Facultades,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.idPrograma
    
    def insert(idPrograma_P,codigo_programa_P,nombre_P,descripcion_P,idFacultad_P):
        P=Programas()
        P.idPrograma=idPrograma_P
        P.codigo_programa=codigo_programa_P
        P.nombre=nombre_P
        P.descripcion=descripcion_P
        P.idFacultad=idFacultad_P
        
       
     
        P.save()
        return "Ha insertado PROGRAMA: "+idPrograma_P+" exitosamente."
    
    def update(idPrograma_P,codigo_programa_P,nombre_P,descripcion_P,idFacultad_P):
        P=Programas()
        P.idPrograma=idPrograma_P
        P.codigo_programa=codigo_programa_P
        P.nombre=nombre_P
        P.descripcion=descripcion_P
        P.idFacultad=idFacultad_P
        
        P.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_P):
        return Roles.objects.filter(idPrograma=id_P).values('idPrograma','codigo_programa',
                                                            'nombre','descripcion','idFacultad')

    def delete(id_P):
        P=Roles.objects.filter(idPrograma=id_P)
        P.delete()
        
        return "Ha borrado a: "+ id_P
    
    






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
    
    def __str__(self):
        return self.idPrograma
    
    def insert(idEstudiante_E,sede_E,tipo_documento_E,nombres_E,apellidos_E
              ,programa_Consecutivo_E,cod_Programa_E,telefono_E,otro_Telefono_E,celular_E
              ,mail_E,mail_institucional_E,investigacion_E,nombre_Investigacion_Trabajo_grado_E,nota_E
              ,password_E,facultad_E,ciclo_E,programa_E):
        E=Estudiantes()
        E.idEstudiante=idEstudiante_E
        E.sede=sede_E
        E.tipo_documento=tipo_documento_E
        E.nombres=nombres_E
        E.apellidos=apellidos_E
        E.programa_Consecutivo=programa_Consecutivo_E
        E.cod_Programa=cod_Programa_E
        E.telefono=telefono_E
        E.otro_Telefono=otro_Telefono_E
        E.celular=celular_E
        E.mail=mail_E
        E.mail_institucional=mail_institucional_E
        E.investigacion=investigacion_E
        E.nombre_Investigacion_Trabajo_grado=nombre_Investigacion_Trabajo_grado_E
        E.nota=nota_E
        E.password=password_E
        E.facultad=facultad_E
        E.ciclo=ciclo_E
        E.programa=programa_E
        
       
     
        E.save()
        return "Ha insertado Estudiante: "+idEstudiante_E+" exitosamente."
    
    def update(idEstudiante_E,sede_E,tipo_documento_E,nombres_E,apellidos_E
              ,programa_Consecutivo_E,cod_Programa_E,telefono_E,otro_Telefono_E,celular_E
              ,mail_E,mail_institucional_E,investigacion_E,nombre_Investigacion_Trabajo_grado_E,nota_E
              ,password_E,facultad_E,ciclo_E,programa_E):
        E=Estudiantes()
        E.idEstudiante=idEstudiante_E
        E.sede=sede_E
        E.tipo_documento=tipo_documento_E
        E.nombres=nombres_E
        E.apellidos=apellidos_E
        E.programa_Consecutivo=programa_Consecutivo_E
        E.cod_Programa=cod_Programa_E
        E.telefono=telefono_E
        E.otro_Telefono=otro_Telefono_E
        E.celular=celular_E
        E.mail=mail_E
        E.mail_institucional=mail_institucional_E
        E.investigacion=investigacion_E
        E.nombre_Investigacion_Trabajo_grado=nombre_Investigacion_Trabajo_grado_E
        E.nota=nota_E
        E.password=password_E
        E.facultad=facultad_E
        E.ciclo=ciclo_E
        E.programa=programa_E
        
        E.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_E):
        return Roles.objects.filter(idEstudiante=id_E).values('idEstudiante','sede',
                                                            'tipo_documento','nombres','apellidos',
                                                            'programa_Consecutivo','cod_Programa','telefono',
                                                            'otro_Telefono','celular','mail','mail_institucional',
                                                            'investigacion','nombre_Investigacion_Trabajo_grado','nota',
                                                            'password','facultad','ciclo','programa')

    def delete(id_E):
        E=Roles.objects.filter(idEstudiante=id_E)
        E.delete()
        
        return "Ha borrado a: "+ id_E


class Sedes(models.Model):
    codigo=models.AutoField(primary_key=True)
    descripcion=models.CharField(max_length=100)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    
    Sedes_Por_Facultad=models.ManyToManyField(Facultades)
    
    def __str__(self):
        return self.codigo
    
    def insert(codigo_S,descripcion_S,direccion_S,telefono_S):
        S=Sedes()
        S.codigo=codigo_S
        S.descripcion=descripcion_S
        S.direccion=direccion_S
        S.telefono=telefono_S
        
       
     
        S.save()
        return "Ha insertado SEDE: "+codigo_S+" exitosamente."
    
    def update(codigo_S,descripcion_S,direccion_S,telefono_S):
        S=Sedes()
        S.codigo=codigo_S
        S.descripcion=descripcion_S
        S.direccion=direccion_S
        S.telefono=telefono_S
        
        S.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_S):
        return Roles.objects.filter(codigo=id_S).values('codigo','descripcion',
                                                            'direccion','telefono')

    def delete(id_S):
        S=Roles.objects.filter(codigo=id_S)
        S.delete()
        
        return "Ha borrado a: "+ id_P

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
    
    def __str__(self):
        return self.idPrograma
    
    def insert(codigo_IES_PR,nombre_IES_PR,año_PR,semestre_PR,titulo_PR
              ,resultados_esperados_PR,nombre_materia_PR,codigo_materia_PR,grupo_materia_PR,nombre_programa_de_materia_estudiante_PR
              ,codigo_programa_de_materia_estudiante_PR,programa_estudiante_PR,codigo_programa_estudiante_PR,tipo_identificacion_PR,nro_identificacion_PR
              ,nombres_PR,rol_PR,rol_Segun_Colciencias_PR,NBC_PR,horas_asignadas_docente_PR
              ,gasto_total_PR,tipo_De_gasto_PR,valor_semana_PR,correo_electronico_PR
              ,tipo_proyecto_PR,idGrupo_investigacion_PR,tipo_participacion_proyecto_PR,maximo_nivel_educativo_PR):
        PR=Proyectos()
        PR.codigo_IES=codigo_IES_PR
        PR.nombre_IES=nombre_IES_PR
        PR.año=año_PR
        PR.semestre=semestre_PR
        PR.titulo=titulo_PR
        PR.resultados_esperados=resultados_esperados_PR
        PR.nombre_materia=nombre_materia_PR
        PR.codigo_materia=codigo_materia_PR
        PR.grupo_materia=grupo_materia_PR
        PR.nombre_programa_de_materia_estudiante=nombre_programa_de_materia_estudiante_PR
        PR.codigo_programa_de_materia_estudiante=codigo_programa_de_materia_estudiante_PR
        PR.programa_estudiante=programa_estudiante_PR
        PR.codigo_programa_estudiante=codigo_programa_estudiante_PR
        PR.tipo_identificacion=tipo_identificacion_PR
        PR.nro_identificacion=nro_identificacion_PR
        PR.nombres=nombres_PR
        PR.rol=rol_PR
        PR.rol_Segun_Colciencias=rol_Segun_Colciencias_PR
        PR.NBC=NBC_PR
        PR.horas_asignadas_docente=horas_asignadas_docente_PR
        PR.gasto_total=gasto_total_PR
        PR.tipo_De_gasto=tipo_De_gasto_PR
        PR.valor_semana=valor_semana_PR
        PR.correo_electronico=correo_electronico_PR
        PR.tipo_proyecto=tipo_proyecto_PR
        PR.idGrupo_investigacion=idGrupo_investigacion_PR
        PR.tipo_participacion_proyecto=tipo_participacion_proyecto_PR
        PR.maximo_nivel_educativo=maximo_nivel_educativo_PR
        
       
     
        PR.save()
        return "Ha insertado PROYECTO: "+codigo_IES_PR+" exitosamente."
    
    def update(codigo_IES_PR,nombre_IES_PR,año_PR,semestre_PR,titulo_PR
              ,resultados_esperados_PR,nombre_materia_PR,codigo_materia_PR,grupo_materia_PR,nombre_programa_de_materia_estudiante_PR
              ,codigo_programa_de_materia_estudiante_PR,programa_estudiante_PR,codigo_programa_estudiante_PR,tipo_identificacion_PR,nro_identificacion_PR
              ,nombres_PR,rol_PR,rol_Segun_Colciencias_PR,NBC_PR,horas_asignadas_docente_PR
              ,gasto_total_PR,tipo_De_gasto_PR,valor_semana_PR,correo_electronico_PR
              ,tipo_proyecto_PR,idGrupo_investigacion_PR,tipo_participacion_proyecto_PR,maximo_nivel_educativo_PR):
        PR=Proyectos()
        
        PR.codigo_IES=codigo_IES_PR
        PR.nombre_IES=nombre_IES_PR
        PR.año=año_PR
        PR.semestre=semestre_PR
        PR.titulo=titulo_PR
        PR.resultados_esperados=resultados_esperados_PR
        PR.nombre_materia=nombre_materia_PR
        PR.codigo_materia=codigo_materia_PR
        PR.grupo_materia=grupo_materia_PR
        PR.nombre_programa_de_materia_estudiante=nombre_programa_de_materia_estudiante_PR
        PR.codigo_programa_de_materia_estudiante=codigo_programa_de_materia_estudiante_PR
        PR.programa_estudiante=programa_estudiante_PR
        PR.codigo_programa_estudiante=codigo_programa_estudiante_PR
        PR.tipo_identificacion=tipo_identificacion_PR
        PR.nro_identificacion=nro_identificacion_PR
        PR.nombres=nombres_PR
        PR.rol=rol_PR
        PR.rol_Segun_Colciencias=rol_Segun_Colciencias_PR
        PR.NBC=NBC_PR
        PR.horas_asignadas_docente=horas_asignadas_docente_PR
        PR.gasto_total=gasto_total_PR
        PR.tipo_De_gasto=tipo_De_gasto_PR
        PR.valor_semana=valor_semana_PR
        PR.correo_electronico=correo_electronico_PR
        PR.tipo_proyecto=tipo_proyecto_PR
        PR.idGrupo_investigacion=idGrupo_investigacion_PR
        PR.tipo_participacion_proyecto=tipo_participacion_proyecto_PR
        PR.maximo_nivel_educativo=maximo_nivel_educativo_PR
        
        PR.save()
        
        return "ha actualizado exitosamente"
    
    def select(id_PR):
        return Roles.objects.filter(codigo_IES=id_PR).values('codigo_IES','nombre_IES',
                                                            'año','semestre','titulo',
                                                            'resultados_esperados','nombre_materia','codigo_materia',
                                                            'grupo_materia','nombre_programa_de_materia_estudiante','codigo_programa_de_materia_estudiante',
                                                            'programa_estudiante','codigo_programa_estudiante','tipo_identificacion',
                                                            'nro_identificacion','nombres','rol',
                                                            'rol_Segun_Colciencias','NBC','horas_asignadas_docente',
                                                            'gasto_total','tipo_De_gasto','valor_semana','correo_electronico',
                                                            'tipo_proyecto','idGrupo_investigacion',
                                                            'tipo_participacion_proyecto','maximo_nivel_educativo')

    def delete(id_PR):
        PR=Roles.objects.filter(codigo_IES=id_PR)
        PR.delete()
        
        return "Ha borrado a: "+ id_PR
    
    
    
    
    
    
    
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