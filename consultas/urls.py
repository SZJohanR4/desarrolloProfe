from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'index/$', views.logeo, name='index'),
    url(r'home/$', views.homeDP, name='homeDP'),
    url(r'index/$', views.logout, name='logout'),
    url(r'crearProyecto/$', views.crearProyecto, name='crearProyecto'),
    url(r'agregarEstudiante/$', views.agregarEstudiante, name='agregarEstudiante'),
   	url(r'registrarUsuarios/$', views.registrarUsuario_view, name='registrarUsuarios'),
   	url(r'registrarInformacion/$', views.registrarInformacion_view, name='registrarInformacion'),
    url(r'listaUsuarios/$', views.listaUsuarios_view, name='listaUsuarios'),
    url(r'misActividades/$', views.listaActividades, name='listaActividades'),
    url(r'infoProyecto/$', views.listaProyectos, name='listaProyectos'),
    url(r'subirActividad/$', views.subirActividad, name='subirActividad'),
    
    url(r'crearActividad/$', views.crearActividad, name='crearActividad'),
    url(r'editarActividad/$', views.editarActividad, name='editarActividad'),
    url(r'eliminarActividad/$', views.eliminarActividad, name='eliminarActividad'),
    url(r'editarProyectoDP/$', views.editarProyectoDP, name='editarProyectoDP'),
    url(r'eliminarProyecto/$', views.eliminarProyecto, name='eliminarProyecto'),
    url(r'buscarProyecto/$', views.buscarProyecto, name='buscarProyecto'),
    url(r'report_usuario/$', views.generar_pdf_usuarios, name= 'report_usuario'),
]