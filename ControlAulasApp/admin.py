from django.contrib import admin
from .models import EstadoAula, Horario, Publicacion, Archivo, RegistroIncidencia, Inventario, RetiroInventario, Aforo


# Register your models here.

@admin.register(EstadoAula)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreSala', 'estado', 'aforo', 'sector')
    # ordering = ('nombreSala')
    # search_fields = ('nombre')
    # list_display_links = ('nombreSala')
    # list_per_page = 3     #paginacion
    list_filter = ('nombreSala', 'estado', 'sector')
    list_editable = ('estado',)

    def datos(self, obj):
        return obj.nombre.upper()


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'asignacion', 'dia', 'hora')
    list_filter = ('dia', 'asignacion', 'apellidosPersonal')
    list_editable = ('dia', 'hora', 'asignacion')

    def datos(self, obj):
        return obj.nombre.upper()


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion')
    list_filter = ('titulo', 'descripcion')

    def datos(self, obj):
        return obj.nombre.upper()


# admin.site.register(EstadoAula)


@admin.register(Archivo)
class ArchivoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion')
    list_filter = ('titulo',)

    def datos(self, obj):
        return obj.nombre.upper()


@admin.register(RegistroIncidencia)
class RegistroIncidenciaAdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'nombreAfectado', 'apellidosAfectado', 'fecha','estado',)
    list_filter = ('apellidosAfectado','estado','apellidosRegistrante',)

    def datos(self, obj):
        return obj.nombre.upper()


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombreProducto', 'cantidadAlmacenada')
    list_filter = ('nombreProducto',)
    list_editable = ('cantidadAlmacenada',)

    def datos(self, obj):
        return obj.nombre.upper()


@admin.register(RetiroInventario)
class RetiroInventarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'fecha', 'hora', 'cantidadUtilizada', 'producto')
    list_filter = ('apellidosPersonal','fecha','producto')

    def datos(self, obj):
        return obj.nombre.upper()


@admin.register(Aforo)
class AforoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'largoGeneral', 'anchoGeneral', 'largoDemarcacion', 'anchoDemarcacion')
    list_filter = ('nombre',)

    def datos(self, obj):
        return obj.nombre.upper()
