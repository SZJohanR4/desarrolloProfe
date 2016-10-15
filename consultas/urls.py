from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'$', views.logeo, name='index'),
    url(r'home/$', views.homeAdmin, name='homeAdmin'),
    url(r'logout/$', views.logout, name='logout'),
    url(r'crearProyecto/$', views.crearProyecto, name='crearProyecto'),
]