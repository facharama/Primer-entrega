from atexit import register
from django.contrib import admin
from .models import empleado,Habilidades
# Register your models here.

admin.site.register (Habilidades)

class empladoAdmin (admin.ModelAdmin):
    list_display =(
        'nombre',
        'apellido',
        'trabajo',
        'Departamento',
    ) 
admin.site.register (empleado,empladoAdmin)
