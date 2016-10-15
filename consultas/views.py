from django.template import RequestContext
from django.shortcuts import render_to_response
from consultas.forms import loginForm
from django.contrib.auth import authenticate, login
from django.forms.forms import Form

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Usuario

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
        message="Datos invalidos"
        context={'message':message}
    return render(request,'consultas/index.html', context)






def homeAdmin(request):
    datosUser=None
    #tenemos que traer el id del user
    context={'datosUser':datosUser}
    return render_to_response('consultas/PaginaPrincipalAdmin.html', )

def crearProyecto(request):
    return render(request,'consultas/CrearProyecto.html')


def logout(request):
    try:
        del request.session['usuario']
        del request.session["nombre"]
    except KeyError:
        pass
        saludo="Gracias por su visita"
        context={'saludo':saludo}
    return render(request,'index.html', context)

