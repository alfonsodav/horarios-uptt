from django.contrib import admin
from .models import Materias, PNF, Profesores, Secciones, Trimestre, Horarios


admin.site.register(Materias)

admin.site.register(PNF)

admin.site.register(Profesores)

admin.site.register(Secciones)

admin.site.register(Trimestre)

admin.site.register(Horarios)
