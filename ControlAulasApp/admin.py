from django.contrib import admin
from .models import EstadoAula, Horario, Publicacion, Archivo


# Register your models here.

@admin.register(EstadoAula)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreSala', 'Estado_Salas')
    # ordering = ('nombreSala')
    # search_fields = ('nombre')
    # list_display_links = ('nombreSala')
    # list_per_page = 3     #paginacion
    # list_editable = ('nombreSala','estado')
    list_filter = ('nombreSala', 'estado')

    def datos(self, obj):
        return obj.nombre.upper()


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'asignacion', 'dia', 'hora')
    list_filter = ('dia', 'asignacion')

    def datos(self, obj):
        return obj.nombre.upper()


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo',)

    # list_filter = ('dia', 'asignacion')

    def datos(self, obj):
        return obj.nombre.upper()
# admin.site.register(EstadoAula)
admin.site.register(Archivo)
