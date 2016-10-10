from django.contrib import admin

from .models import Roles
admin.site.register(Roles)

from .models import Usuarios
admin.site.register(Usuarios)

from .models import Grupos_De_Investigacion
admin.site.register(Grupos_De_Investigacion)

from .models import Centro_investigacion
admin.site.register(Centro_investigacion)

from .models import Noticias
admin.site.register(Noticias)

from .models import Lineas_Investigacion
admin.site.register(Lineas_Investigacion)

from .models import Fuentes_de_Financiacion
admin.site.register(Fuentes_de_Financiacion)

from .models import Tipos_Proyectos
admin.site.register(Tipos_Proyectos)

from .models import Maximo_Nivel_Educativo
admin.site.register(Maximo_Nivel_Educativo)

from .models import tipo_Participacion_Proyecto
admin.site.register(tipo_Participacion_Proyecto)


from .models import Facultades
admin.site.register(Facultades)

from .models import Ciclos
admin.site.register(Ciclos)

from .models import Programas
admin.site.register(Programas)

from .models import Sedes
admin.site.register(Sedes)


from .models import Proyectos
admin.site.register(Proyectos)

from .models import Estudiantes
admin.site.register(Estudiantes)

from .models import Productos_de_Investigacion
admin.site.register(Productos_de_Investigacion)

from .models import Investigadores_De_IES
admin.site.register(Investigadores_De_IES)

from .models import Redes_de_Coperacion
admin.site.register(Redes_de_Coperacion)

from .models import Sector
admin.site.register(Sector)

from .models import Integrantes_de_red
admin.site.register(Integrantes_de_red)


