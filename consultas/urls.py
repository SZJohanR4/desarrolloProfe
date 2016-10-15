from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'index/$', views.logeo, name='index'),
    url(r'crearProyecto/$', views.crearProyecto, name='crearProyecto'),
]