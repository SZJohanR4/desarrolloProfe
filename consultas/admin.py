from django.contrib import admin

from .models import Usuario
admin.site.register(Usuario)

from .models import Grupo_De_Investigacion
admin.site.register(Grupo_De_Investigacion)


from .models import Noticia
admin.site.register(Noticia)

from .models import Linea_Investigacion
admin.site.register(Linea_Investigacion)

from .models import Fuente_de_Financiacion
admin.site.register(Fuente_de_Financiacion)

from .models import Tipo_Proyecto
admin.site.register(Tipo_Proyecto)

from .models import Maximo_Nivel_Educativo
admin.site.register(Maximo_Nivel_Educativo)

from .models import tipo_Participacion_Proyecto
admin.site.register(tipo_Participacion_Proyecto)


from .models import Facultad
admin.site.register(Facultad)

from .models import Ciclo
admin.site.register(Ciclo)

from .models import Programa
admin.site.register(Programa)

from .models import Sede
admin.site.register(Sede)

from .models import Proyecto
admin.site.register(Proyecto)

from .models import Estudiante
admin.site.register(Estudiante)

from .models import Producto_de_Investigacion
admin.site.register(Producto_de_Investigacion)


from .models import Red_de_Coperacion
admin.site.register(Red_de_Coperacion)