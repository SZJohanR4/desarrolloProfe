from django.template import RequestContext
from django.shortcuts import render_to_response
from consultas.forms import loginForm
from django.contrib.auth import authenticate, login
from django.forms.forms import Form

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Usuario, Actividad, Estudiante, Proyecto, Noticia
from consultas.models import Usuario
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
    return render(request,'consultas/CrearProyecto.html')



def crearActividad(request):
    proyectos=Proyecto.objects.filter(directorDeProyecto=request.session["usuario"])
    if request.method=="POST":
        actividad=Actividad()
        
        try:
            actividad.nombre=request.POST['nombreActividad']
            actividad.descripcion=request.POST['descripcion']
            actividad.fecha_Limite=request.POST['fechaLimite']
            actividad.nota=request.POST['nota']
          #  actividad.adjunto=
            user=Usuario.objects.get(usuario= request.session["usuario"])
            estudiante=Estudiante.objects.get(id=request.POST['idEstudiante'])
            proyecto=Proyecto.objects.get(id=request.POST['idProyecto'])
            actividad.idDirector=user
            actividad.idEstudiante=estudiante
            actividad.idProyecto=proyecto
            actividad.save()
            return render(request,"consultas/PaginaPrincipalDirProyecto.html")
        except KeyError:
            message="error no inserto bien los datos" + KeyError
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
            actividad.nota=request.POST['nota']
          #  actividad.adjunto=
            user=Usuario.objects.get(usuario=request.session["usuario"])
            estudiante=Estudiante.objects.get(id=request.POST['idEstudiante'])
            proyecto=Proyecto.objects.get(id=request.POST['idProyecto'])
            actividad.idDirector=user
            actividad.idEstudiante=estudiante
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
    if request.method == "POST":
        noticiaNew=Noticia()
        try:
            noticiaNew.titulo=request.POST['titulo']
            noticiaNew.contenido=request.POST['contenido']
            noticiaNew.fecha_Publicacion=request.POST['fecha_Publicacion']
            userNoticia=Usuario.objects.get(usuario=request.POST['idPropietario'])
            noticiaNew.idPropietario=userNoticia
            noticiaNew.save()
            return render(request,"consultas/PaginaPrincipalAdmin.html") 
        except KeyError:
            datosUser=KeyError
            context={'datosUser':datosUser}
            return render(request,"consultas/PaginaPrincipalAdmin.html")
    else:
        return render(request,'consultas/registrarInformacion.html')



def listaUsuarios_view(request):

    usuarios= Usuario.objects.all()    
    contexto = {'listUsuarios':usuarios}
    return render(request,'consultas/listaUsuarios.html', contexto)

        
