from django.template import RequestContext
from django.shortcuts import render_to_response
from consultas.forms import loginForm
from django.contrib.auth import authenticate, login
from django.forms.forms import Form

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Usuario, Actividad, Estudiante, Proyecto
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
    #message=request.session['usuario']
    #context={'message':message}
    
    if request.method=="POST":
        actividad=Actividad()
        try:
            actividad.nombre=request.POST['nombreActividad']
            actividad.descripcion=request.POST['descripcion']
            actividad.fecha_Limite=request.POST['fechaLimite']
            actividad.nota=request.POST['nota']
          #  actividad.adjunto=
            user=Usuario.objects.get(usuario=request.POST['idDirector'])
            estudiante=Estudiante.objects.get(id=request.POST['idEstudiante'])
            proyecto=Proyecto.objects.get(id=request.POST['idProyecto'])
            actividad.idDirector=user
            actividad.idEstudiante=estudiante
            actividad.idProyecto=proyecto
            actividad.save()
        except KeyError:
            datosUser=KeyError
            context={'datosUser':datosUser}
            return render(request,"consultas/PaginaPrincipalDirProyecto.html")
    else:
        return render(request,'consultas/crearActividad.html')

def logout(request):
    try:
        del request.session['usuario']
        del request.session["nombre"]
    except KeyError:
        pass
        saludo="Gracias por su visita"
        
    return render(request,'consultas/index.html')
    