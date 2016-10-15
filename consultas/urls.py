from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'index/$', views.logeo, name='index'),
    url(r'home/$', views.homeDP, name='homeDP'),
    url(r'logout/$', views.logout, name='logout'),
    url(r'crearProyecto/$', views.crearProyecto, name='crearProyecto'),
    url(r'crearActividad/$', views.crearActividad, name='crearActividad'),
    
]