from django.template import RequestContext
from django.shortcuts import render_to_response
from consultas.forms import loginForm
from django.contrib.auth import authenticate, login
from django.forms.forms import Form

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import consultas
# Create your views here.




def index(request):
    message=None
    datos=None
    if request.method=="POST":#mi request bien con datos
        form=loginForm(request.POST)#le paso los datos del formulario
        if form.is_valid():#pregunto si los datos del form son validos
            nombreLlega=request.POST['user']
            passLlega=request.POST['pass']
            tipoLlega=request.POST['tipo']
            user=authenticate(username=nombreLlega, password=passLlega, tipo=tipoLlega)
            datos=nombreLlega+" el nombre y la pass  "+ passLlega
            if user is not None:
                if user.is_active:
                    login(request, user)
                    message= "te has identificado de modo correcto ->"+nombreLlega+"  "+passLlega
                else:
                    message= "tu usuario es inactivo"
            else:
                message="nombre usuer y pass incorrecto"
    else:
        form=loginForm()
    
    context={'message':message,'datos':datos}
   # template=loader.get_template('consultas/logearse.html')
    return render(request,'gui/index.html', context)

def pagPrincAdmin(request):
    return render(request, 'gui/paginaPrincipalAdmin.html')

def pagPrincDirProyecto(request):
    return render(request, 'gui/paginaPrincipalDirProyecto.html')

def pagPrincEstudiante(request):
    return render(request, 'gui/pagPrincEstudiante.html')