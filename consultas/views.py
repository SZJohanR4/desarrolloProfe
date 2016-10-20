from django.template import RequestContext
from django.shortcuts import render_to_response
from consultas.forms import loginForm
from django.contrib.auth import authenticate, login
from django.forms.forms import Form
from io import BytesIO
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Usuario, Actividad,Actividad_Estudiante, Sede, Facultad, Ciclo, Programa, Estudiante, Proyecto, Noticia, tipo_Participacion_Proyecto, Tipo_Proyecto, Grupo_De_Investigacion, Linea_Investigacion,Nucleo_Basico_Conocimiento,Maximo_Nivel_Educativo,Fuente_de_Financiacion,Red_de_Coperacion
from consultas.models import Usuario
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Table
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
# Create your views here.




def logeo(request):
    message="ingrse los datos"
    saludo=None
    if request.method=="POST":#mi request bien con datos
        form=loginForm(request.POST)#le paso los datos del formulario
        
        if form.is_valid():#pregunto si los datos del form son validos
            try:
                user=Usuario.objects.get(usuario=request.POST['user'])
                if user.password==request.POST['password']:
                    if user.rol==request.POST['tipo']:
                        if user.rol=="Administrador":
                            request.session["usuario"]=user.usuario
                            request.session["nombre"]=user.nombre
                            return render(request,"consultas/PaginaPrincipalAdmin.html")
                        else:
                            if user.rol=="Director de Proyecto":
                                request.session["usuario"]=user.usuario
                                request.session["nombre"]=user.nombre
                            
                                return render(request,"consultas/PaginaPrincipalDirProyecto.html")
                            else:
                                if user.rol=="Estudiante":
                                    request.session["usuario"]=user.usuario
                                    request.session["nombre"]=user.nombre
                                    return render(request,"consultas/PaginaPrincipalEstudiante.html")
                    else:
                         message="usted no es un "+ request.POST['tipo']
                         context={'message':message}
                         return render(request,"consultas/index.html",context)                            
                else:
                    message="contraseña incorrecta"
                    context={'message':message}
                    return render(request,"consultas/index.html",context)
            except Usuario.DoesNotExist:
                message="Usuario no registrado"
                context={'message':message}
                return render(request,"consultas/index.html",context)
    else:
        form=loginForm()
    return render(request,'consultas/index.html')






def homeDP(request):
    return render(request,"consultas/PaginaPrincipalDirProyecto.html")

def crearProyecto(request):
    if request.method == "POST":
        proyecto=Proyecto()
        try:
            proyecto.nombreMacroProyecto=request.POST['nombreMacroProyecto']
            proyecto.nombre_IES=request.POST['nombreProyecto']
            proyecto.objetivo_proyecto=request.POST['objetivo']
            proyecto.sublinea=request.POST['sublinea']
            proyecto.empresa=request.POST['empresa']
            tipo_proyecto_copia=Tipo_Proyecto.objects.get(nombre=request.POST['producto'])
            proyecto.tipo_proyecto=tipo_proyecto_copia
            proyecto.perfiles=request.POST['perfiles']
            directorDeProyecto_copia=Usuario.objects.get(usuario=request.POST['nombreDirector'])
            proyecto.directorDeProyecto=directorDeProyecto_copia
            proyecto.nombreJurados=request.POST['nombreJurados']
            proyecto.save()
            return render(request,"consultas/PaginaPrincipalAdmin.html")
        except KeyError:
            datosUser=KeyError
            context={'datosUser':datosUser}
            return render(request,"consultas/PaginaPrincipalAdmin.html")
    else:
        tipo_proyectos= Tipo_Proyecto.objects.all()
        director=Usuario.objects.filter(rol='Director de Proyecto')
        context={'list_tipoProyectos':tipo_proyectos, 'listDirector':director}
        return render(request,'consultas/CrearProyecto.html',context)

def agregarEstudiante(request):
    if request.method == 'POST':
        estudiante=Estudiante()
        usuario=Usuario()
        try:
            # Agregar en la tabla Usuario
            usuario.usuario=request.POST['usuario']
            usuario.nombre= request.POST['nombre']
            usuario.apellido= request.POST['apellido']
            usuario.password= request.POST['password']
            usuario.documento= request.POST['documento']
            usuario.telefono= request.POST['telefono']
            usuario.celular= request.POST['celular']
            usuario.mail= request.POST['mail']
            usuario.mail_institucional= request.POST['mailInstitucional']
            usuario.facultad= request.POST['facultad']
            usuario.rol='Estudiante'
            usuario.save()
            # Agregar en la tabla Estudiante
            estudiante.usuario=request.POST['usuario']
            estudiante.tipo_documento=request.POST['tipoDocumento']
            estudiante.nombres= request.POST['nombre']
            estudiante.apellidos= request.POST['apellido']
            estudiante.password= request.POST['password']
            estudiante.documento= request.POST['documento']
            estudiante.telefono= request.POST['telefono']
            estudiante.otro_Telefono= request.POST['otroTelefono']
            estudiante.celular= request.POST['celular']
            estudiante.mail= request.POST['mail']
            estudiante.mail_institucional= request.POST['mailInstitucional']
            estudiante.investigacion=request.POST['investigacion']
            estudiante.rol='Estudiante'
            sede_copia=Sede.objects.get(nombre=request.POST['sede'])
            estudiante.sede=sede_copia
            facultad_copia=Facultad.objects.get(nombre=request.POST['facultad'])
            estudiante.facultad=facultad_copia
            ciclo_copia=Ciclo.objects.get(nombre=request.POST['ciclo'])
            estudiante.ciclo=ciclo_copia
            programa_copia=Programa.objects.get(nombre=request.POST['programa'])
            estudiante.programa=programa_copia
            proyecto_copia=Proyecto.objects.get(id=request.POST['idProyecto'])
            estudiante.proyecto=proyecto_copia
            estudiante.save()
            return render(request,"consultas/PaginaPrincipalAdmin.html")
        except KeyError:
            datosUser=KeyError
            context={'datosUser':datosUser}
            return render(request,'consultas/PaginaPrincipalAdmin.html',context)
    else:
        proyectos= Proyecto.objects.all()
        sedes= Sede.objects.all()
        facultad=Facultad.objects.all()
        ciclos=Ciclo.objects.all()
        programas=Programa.objects.all()
        contexto = {'listProyectos':proyectos, 'listSedes':sedes, 'listFacultad':facultad, 'listCiclos':ciclos, 'listProgramas':programas}
        return render(request,'consultas/AgregarEstudiante.html',contexto)

        
def crearActividad(request):
    proyectos=Proyecto.objects.filter(directorDeProyecto=request.session["usuario"])
    if request.method=="POST":
        actividad=Actividad()
        
        try:
            actividad.nombre=request.POST['nombreActividad']
            actividad.descripcion=request.POST['descripcion']
            actividad.fecha_Limite=request.POST['fechaLimite']
          #  actividad.adjunto=
            user=Usuario.objects.get(usuario= request.session["usuario"])
            proyecto=Proyecto.objects.get(id=request.POST['idProyecto'])
            actividad.idDirector=user
            actividad.idProyecto=proyecto
            actividad.save()
            return render(request,"consultas/PaginaPrincipalDirProyecto.html")
        except KeyError:
            message="error no inserto bien los datos"
            context={'datosUser':message}
            return render(request,"consultas/PaginaPrincipalDirProyecto.html")
    else:
        context={'listaProyectos':proyectos}
        return render(request,'consultas/crearActividad.html',context)

    
def editarActividad(request):
    actividades=Actividad.objects.filter(idDirector=request.session["usuario"])
    proyectos=Proyecto.objects.filter(directorDeProyecto=request.session["usuario"])
    if request.method=="POST":
        try:
            message="datos ingresados correctamentte"
            actividad=Actividad()
            actividad.id=request.POST['idActividad']
            actividad.nombre=request.POST['nombreActividad']
            actividad.descripcion=request.POST['descripcion']
            actividad.fecha_Limite=request.POST['fechaLimite']
          #  actividad.adjunto=
            user=Usuario.objects.get(usuario=request.session["usuario"])
            proyecto=Proyecto.objects.get(id=request.POST['idProyecto'])
            actividad.idDirector=user
            actividad.idProyecto=proyecto
            actividad.save()
            context={'datosUser':message}
            return render(request,"consultas/PaginaPrincipalDirProyecto.html",context)
        except KeyError:
            message="error no inserto bien los datos" 
            context={'datosUser':message}
            return render(request,"consultas/PaginaPrincipalDirProyecto.html",context)
    else:
        context={'listaProyectos':proyectos, 'listaActividaddes':actividades}
        return render(request,'consultas/editarActividad.html',context)

def eliminarActividad(request):
    actividades=Actividad.objects.filter(idDirector=request.session["usuario"])
    if request.method=="POST":
        actividad=Actividad()
        actividad.id=request.POST['idActividad']
        actividad.delete()
        message="actividad eliminada correctamente"
        context={'datosUser':message}
        return render(request,"consultas/PaginaPrincipalDirProyecto.html",context)
    else:
       context={'listaActividaddes':actividades}
       return render(request,'consultas/eliminarActividad.html',context)

def buscarProyecto(request):
    if request.method=="POST":
        proyectoNombre=Proyecto.objects.filter(nombre_IES=request.POST['buscarProyecto'],directorDeProyecto=request.session['usuario'])
        proyectoUsuario=Proyecto.objects.filter(directorDeProyecto=request.session['usuario'])
        context={'listaProyecto':proyectoNombre,'listaUsuario':proyectoUsuario}
        return render(request,"consultas/buscarProyectos.html",context)
    else:
        proyectoUsuario=Proyecto.objects.filter(directorDeProyecto=request.session['usuario'])
        context={'listaUsuario':proyectoUsuario}
        return render(request,"consultas/buscarProyectos.html",context)

def eliminarProyecto(request):
    proyectos=Proyecto.objects.filter(directorDeProyecto=request.session["usuario"])
    if request.method=="POST":
        proyecto=Proyecto()
        proyecto.id=request.POST['idProyecto']
        proyecto.delete()
        message="actividad eliminada correctamente"
        context={'datosUser':message}
        return render(request,"consultas/PaginaPrincipalDirProyecto.html",context)
    else:
        context={'listaProyectos':proyectos}
    return render(request,"consultas/eliminarProyecto.html",context)




def editarProyectoDP(request):
    proyectos=Proyecto.objects.filter(directorDeProyecto=request.session["usuario"])
    grupo_inves=Grupo_De_Investigacion.objects.all()
    linea_invs=Linea_Investigacion.objects.all()
    ti_parti_proy=tipo_Participacion_Proyecto.objects.all()
    nbc=Nucleo_Basico_Conocimiento.objects.all()
    max_nivel_educa=Maximo_Nivel_Educativo.objects.all()
    fuente_financia=Fuente_de_Financiacion.objects.all()
    dirProyect=Usuario.objects.filter(usuario=request.session["usuario"])
    red_inves=Red_de_Coperacion.objects.all()
    if request.method=="POST":
      #  try:
        
        proyecto=Proyecto()
        proyecto.id=request.POST['idProyecto']

        # proyectoParteAdmin=Proyecto.objects.filter(id=request.POST['idProyecto'])
        # datos={'listProyectoParteAdmin':proyectoParteAdmin}
        # for proyectoParteAdmin in listProyectoParteAdmin:
        #     proyecto.nombreMacroProyecto=proyectoParteAdmin.nombreMacroProyecto
        #     proyecto.nombre_IES=proyectoParteAdmin.nombre_IES
        #     proyecto.objetivo_proyecto=proyectoParteAdmin.objetivo_proyecto
        #     proyecto.sublinea=proyectoParteAdmin.sublinea
        #     proyecto.empresa=proyectoParteAdmin.empresa
        #     tipo_proyecto_copia=Tipo_Proyecto.objects.get(nombre=proyectoParteAdmin.tipo_proyecto)
        #     proyecto.tipo_proyecto=tipo_proyecto_copia
        #     proyecto.perfiles=proyectoParteAdmin.perfiles
        #     proyecto.nombreJurados=proyectoParteAdmin.nombreJurados


        proyecto.codigo_IES=request.POST['codigoIES']
        # proyecto.nombreMacroProyecto=request.POST['nombreMacroP']
        proyecto.ano=request.POST['ano']
        proyecto.semestre=request.POST['semestre']
        proyecto.titulo=request.POST['titulo']
        proyecto.fecha_inicio=request.POST['fecha_inicio']
        proyecto.duracion=request.POST['duracion']
        proyecto.sede=request.POST['sede']
        proyecto.nombre_materia=request.POST['nombre_materia']
        proyecto.codigo_materia=request.POST['codigo_materia']
        proyecto.grupo_materia=request.POST['grupo_materia']
        proyecto.objetivo_socioeconomico=request.POST['objetivo_socioeconomico']
        # proyecto.objetivo_proyecto=request.POST['objetivo_proyecto']
        proyecto.resumen_proyecto=request.POST['resumen_proyecto']
        proyecto.resultados_esperados=request.POST['resultados_esperados']
        
        proyecto.horas_asignadas_docente=request.POST['horas_asignadas_docente']
        proyecto.gasto_total=request.POST['gasto_total']
        proyecto.tipo_De_gasto=request.POST['tipo_De_gasto']
        proyecto.valor_semana=request.POST['valor_semana']
        # proyecto.sublinea=request.POST['sublinea']
        proyecto.empresa=request.POST['empresa']
        # proyecto.nombreJurados=request.POST['nombreJurados']
        proyecto.perfiles=request.POST['perfiles']
        proyecto.realizo_Sustentacion_publica=request.POST['realizo_Sustentacion_publica']
        proyecto.otras_Entidades_Participantes=request.POST['otras_Entidades_Participantes']
        proyecto.realizo_Sustentacion_publica=request.POST['realizo_Sustentacion_publica']
        proyecto.asociado_al_area_de_conocimiento=request.POST['asociado_al_area_de_conocimiento']
        proyecto.finalizado=request.POST['finalizado']
        proyecto.paz_y_salvo=request.POST['paz_y_salvo']
        proyecto.modalidad_de_seminario=request.POST['modalidad_de_seminario']
        proyecto.realizo_Sustentacion_publica=request.POST['realizo_Sustentacion_publica']
        
        # tipoProyectoObj=Tipo_Proyecto.objects.get(nombre=request.POST['tipoProyecto'])
        grupoInvestigacionObj=Grupo_De_Investigacion.objects.get(id=request.POST['grupoInves'])
        lineaInvstObj=Linea_Investigacion.objects.get(id=request.POST['lineaInvesti'])
        tipoParticipacionObj=tipo_Participacion_Proyecto.objects.get(id=request.POST['tipoParticipacionProyecto'])
        nbcObj=Nucleo_Basico_Conocimiento.objects.get(id=request.POST['nucleoBasic'])
        maxNivelEduObj=Maximo_Nivel_Educativo.objects.get(id=request.POST['maximoNivelEducativo'])
        fuenteFinanciaObj=Fuente_de_Financiacion.objects.get(id=request.POST['fuenteFinancia'])
        dirProyectObj=Usuario.objects.get(usuario=request.session['usuario'])
        redInvestigaObje=Red_de_Coperacion.objects.get(id=request.POST['redInvestigacion'])
        
        # proyecto.tipo_proyecto=tipoProyectoObj
        proyecto.idGrupo_investigacion=grupoInvestigacionObj
        proyecto.id_lineas_investigacion_asociadas=lineaInvstObj
        proyecto.tipo_participacion_proyecto=tipoParticipacionObj
        proyecto.NBC=nbcObj
        proyecto.maximo_nivel_educativo=maxNivelEduObj
        proyecto.Fuente_de_financiacion=fuenteFinanciaObj
        proyecto.directorDeProyecto=dirProyectObj
        proyecto.red_investigacion=redInvestigaObje
        proyecto.save()
        message="datos insertados c"
        context={'datosUser':message}
        return render(request,"consultas/PaginaPrincipalDirProyecto.html")
        #except KeyError:
         #   message="error no inserto bien los datos" 
         #   context={'datosUser':message}
         #   return render(request,"consultas/PaginaPrincipalDirProyecto.html",context)
    else:
        context={'listaProyectos':proyectos,'lisGrupoInv':grupo_inves,'listLineasInv':linea_invs,
                 'lisTipoParticipacion':ti_parti_proy,'listNbc':nbc, 'listMaxNivelEdu':max_nivel_educa,
                 'listFuenteFinancia':fuente_financia,'listDirProyect':dirProyect,'listRedInvest':red_inves}
        return render(request,'consultas/editarProyectoDP.html',context)


def editarUsuario(request):
    usuarios=Usuario.objects.all()
    if request.method=="POST":
        try:
           
            usuario=Usuario()
            usuario.usuario=request.POST['idUsuario']
            usuario.nombre=request.POST['nombre']
            usuario.apellido=request.POST['apellido']
            usuario.password=request.POST['password']
            usuario.documento=request.POST['documento']
            usuario.telefono=request.POST['telefono']
            usuario.celular=request.POST['celular']
            usuario.mail=request.POST['mail']
            usuario.mail_institucional=request.POST['mail_institucional']
            usuario.facultad=request.POST['facultad']
            usuario.nro_Proyectos_a_Cargo=request.POST['nro_Proyectos_a_Cargo']
            usuario.rol=request.POST['rol']
            usuario.usuario=request.POST['idUsuario']
            usuario.save()
            message="datos ingresados correctamentte"
            context={'datosUser':message}
            return render(request,"consultas/PaginaPrincipalAdmin.html",context)
        except KeyError:
            message="error no inserto bien los datos" 
            context={'datosUser':message}
            return render(request,"consultas/PaginaPrincipalAdmin.html",context)
    else:
       context={'listaUsuarios':usuarios}
       return render(request,'consultas/editarUsuario.html',context)

def eliminarUsuario(request):
    usuarios=Usuario.objects.all()
    if request.method=="POST":
        usuario=Usuario()
        usuario.usuario=request.POST['idUsuario']
        usuario.delete()
        message="Usuario eliminada correctamente"
        context={'datosUser':message}
        return render(request,"consultas/PaginaPrincipalAdmin.html",context)
    else:
        context={'listaUsuarios':usuarios}
    return render(request,"consultas/eliminarUsuarios.html",context)



def logout(request):
    try:
        del request.session['usuario']
        del request.session["nombre"]
    except KeyError:
        pass
        saludo="Gracias por su visita"
        
    return render(request,'consultas/index.html')


def registrarUsuario_view(request):
    if request.method == "POST":
        usuario=Usuario()
        try:
            usuario.usuario=request.POST['usuario']
            usuario.nombre= request.POST['nombre']
            usuario.apellido= request.POST['apellido']
            usuario.password= request.POST['password']
            usuario.documento= request.POST['documento']
            usuario.telefono= request.POST['telefono']
            usuario.celular= request.POST['celular']
            usuario.mail= request.POST['mail']
            usuario.mail_institucional= request.POST['mail_institucional']
            usuario.facultad= request.POST['facultad']
            usuario.nro_Proyectos_a_Cargo= request.POST['nro_proyectos_a_cargo']
            usuario.rol=request.POST['rol']
            usuario.save()
            return render(request,"consultas/PaginaPrincipalAdmin.html")   
        except KeyError:
            datosUser=KeyError
            context={'datosUser':datosUser}
            return render(request,"consultas/PaginaPrincipalAdmin.html")
    else:
        return render(request,'consultas/registrarUsuarios.html')


def registrarInformacion_view(request):
    usuario=Usuario.objects.filter(usuario=request.session["usuario"])
    if request.method == "POST":
        noticiaNew=Noticia()
        try:
            noticiaNew.titulo=request.POST['titulo']
            noticiaNew.contenido=request.POST['contenido']
            noticiaNew.fecha_Publicacion=request.POST['fecha_Publicacion']
            userNoticia=Usuario.objects.get(usuario=request.session['usuario'])
            noticiaNew.idPropietario=userNoticia
            noticiaNew.save()
            return render(request,"consultas/PaginaPrincipalAdmin.html") 
        except KeyError:
            datosUser=KeyError
            context={'datosUser':datosUser}
            return render(request,"consultas/PaginaPrincipalAdmin.html")
    else:
        context={'listUsuario':usuario}
        return render(request,'consultas/registrarInformacion.html',context)



def listaUsuarios_view(request):
    usuarios= Usuario.objects.all()    
    contexto = {'listUsuarios':usuarios}
    return render(request,'consultas/listaUsuarios.html', contexto)


def listaActividades(request):
    actividades = Actividad.objects.all()
    contexto = {'listActividades':actividades}
    return render(request,'consultas/misActividades.html',contexto)

def listaProyectos(request):
    proyectos = Proyecto.objects.all()
    contexto = {'listProyectos':proyectos}
    return render(request,'consultas/ConsultarInfoProyecto.html',contexto)

def subirActividad(request):
    usuario_estudiante=Estudiante.objects.filter(usuario=request.session["usuario"])
    if request.method == "POST":
        actividad=Actividad_Estudiante()
        try:
            actividad.desarrollo=request.POST['desarrollo']
            actividad.adjunto=request.POST['desarrolloAdjunto']
            idActividad_copia=Actividad.objects.get(id=request.POST['idActividad'])
            actividad.idActividad=idActividad_copia
            idEstudiante_copia=Estudiante.objects.get(usuario=request.session["usuario"])
            actividad.UsuarioEstudiante=idEstudiante_copia
            actividad.save()
            return render(request,"consultas/PaginaPrincipalEstudiante.html")   
        except KeyError:
            datosUser=KeyError
            context={'datosUser':datosUser}
            return render(request,"consultas/PaginaPrincipalEstudiante.html")   
    else:
        actividades=Actividad.objects.all()
        context={'listActividades':actividades,'listEstudiante':usuario_estudiante}
        return render(request,'consultas/SubirActividad.html',context)

def generar_pdf_usuarios(request):

    response = HttpResponse(content_type='application/pdf')
    pdf_name = "Usuarios.pdf"  # llamado clientes
    # la linea 26 es por si deseas descargar el pdf a tu computadora
    # response['Content-Disposition'] = 'attachment; filename=%s' % pdf_name
    buff = BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    clientes = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Usuarios", styles['Heading1'] , "Unipanamericana",)

    clientes.append(header)
    headings = ('Nombre', 'Apellido', 'Documento','Celuar', 'Mail', ' Mail Institucional', 'Rol' )
    high = 650
    allclientes = [( p.nombre, p.apellido, p.documento, p.celular, p.mail, p.mail_institucional, p.rol) for p in Usuario.objects.all()]
    

    t = Table([headings] + allclientes)
    t.setStyle(TableStyle(
        [
                    
        ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black), ]))
        
   
    clientes.append(t)
    doc.build(clientes)
    response.write(buff.getvalue())
    buff.close()
    return response

def paginaPrincipalAdmin(request):
    return render(request,'consultas/PaginaPrincipalAdmin.html')

def PaginaPrincipalDirProyecto(request):
    return render(request,'consultas/PaginaPrincipalDirProyecto.html')


def PaginaPrincipalEstudiante(request):
    return render(request,'consultas/PaginaPrincipalEstudiante.html')