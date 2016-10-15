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
    message=None
    datos=None
    context={'message':message,'datos':datos}
    if request.method=="POST":#mi request bien con datos
       
        form=loginForm(request.POST)#le paso los datos del formulario
        if form.is_valid():#pregunto si los datos del form son validos
            nombreLlega=request.POST['user']
            passLlega=request.POST['password']
            tipoLlega=request.POST['tipo']
            
            
            if Usuario.objects.get(nombre=nombreLlega, password=passLlega, rol=tipoLlega):
                user=authenticate(nombre=nombreLlega, password=passLlega)
                message=user
                context={'message':message,'datos':datos}
                return render(request,'consultas/PaginaPrincipalAdmin.html', context)
            else:
               datos=form.errors
    else:
        form=loginForm()
    context={'message':message,'datos':datos}
    return render(request,'consultas/index.html', context)


def homeAdmin(request):
    datosUser=None
    #tenemos que traer el id del user
    context={'datosUser':datosUser}
    return render_to_response('consultas/PaginaPrincipalAdmin.html', )



def pagPrincAdmin(request):
    return render(request, 'gui/paginaPrincipalAdmin.html')

def pagPrincDirProyecto(request):
    return render(request, 'gui/paginaPrincipalDirProyecto.html')

def pagPrincEstudiante(request):
    return render(request, 'gui/pagPrincEstudiante.html')