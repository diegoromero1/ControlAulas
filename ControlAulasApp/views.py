# Create your views here.
import os

from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView

from ControlAulas import settings
from ControlAulasApp.forms import PasswordChangingForm, HorarioForm, RegistroIncidenciaForm, AgregarIncidenciaForm, \
    InventarioForm, RetiroInventarioForm, AforoForm
from ControlAulasApp.models import EstadoAula, Horario, Publicacion, Archivo, RegistroIncidencia, Inventario, \
    RetiroInventario, Aforo
import logging


def IndexView(request):
    publicaciones = Publicacion.objects.all()
    data = {
        'publicaciones': publicaciones
    }

    return render(request, 'ControlAulasApp/index.html', data)


# Cambio de contrasena
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, 'accounts/password_success.html', {})


def Estados(request):
    tablaEstados = EstadoAula.objects.all()
    # tablaEstados = EstadoAula.objects.all()[:5] #mostrar los primeros 5
    # tablaEstados = EstadoAula.objects.all().order_by('nombreSala') #ordenar por nombre
    # tablaEstados = EstadoAula.objects.filter(nombre= 'sala') #filtar datos

    # page = request.GET.get('page', 1)
    #
    # try:
    #     paginator = Paginator(tablaEstados, 10)
    #     tablaEstados = paginator.page(page)
    # except:
    #     raise Http404

    data = {
        'titulo': 'Estado de salas',
        'entity': tablaEstados,
        # 'paginator': paginator
    }
    # return render(request, "ControlAulasApp/estadoaulas.html",{"estados": tablaEstados})
    return render(request, "ControlAulasApp/estadoaulas.html", data)


# Vista asociada a la visualizacion del horario
def Horarios(request):
    tablaHorarios = Horario.objects.all()

    data = {
        'titulo': 'Horario de desinfeccion',
        'entity': tablaHorarios,
    }

    return render(request, "ControlAulasApp/horario.html", data)


class HorariosListView(ListView):
    model = Horario
    template_name = 'ControlAulasApp/horario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Horario de desinfeccion'
        return context


# vista para registrar y editar las observaciones
def edicion_tabla(request, id):
    horario = get_object_or_404(Horario, id=id)

    data = {
        'form': HorarioForm(instance=horario)
    }

    if request.method == 'POST':
        formulario = HorarioForm(data=request.POST, instance=horario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="horario")
        data["form"] = formulario

    return render(request, "ControlAulasApp/edicionTabla.html", data)


# Vista asociada a la descarga de archivos
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), content_type="adminupload")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response

    raise Http404


def descarga(request):
    archivo = Archivo.objects.all()

    context = {
        'entity': archivo,

    }
    return render(request, 'ControlAulasApp/descarga.html', context)


def RegistroIncidencias(request):
    tablaRegistros = RegistroIncidencia.objects.all()

    data = {
        'titulo': 'Registro de incidencias',
        'entity': tablaRegistros,

    }

    return render(request, "ControlAulasApp/incidencias.html", data)


def edicion_tabla_incidencias(request, id):
    incidencia = get_object_or_404(RegistroIncidencia, id=id)

    data = {
        'form': RegistroIncidenciaForm(instance=incidencia)
    }

    if request.method == 'POST':
        formulario = RegistroIncidenciaForm(data=request.POST, instance=incidencia, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="incidencias")
        data["form"] = formulario

    return render(request, "ControlAulasApp/edicionTablaIncidencia.html", data)


def agregarIncidencia(request):
    data = {
        'form': AgregarIncidenciaForm()
    }

    if request.method == 'POST':
        formulario = AgregarIncidenciaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Se agrego correctamente")
            return redirect(to="incidencias")
        data["form"] = formulario

    return render(request, "ControlAulasApp/agregarIncidencia.html", data)


def Inventarios(request):
    tablaInventario = Inventario.objects.all()
    tablaRetiro = RetiroInventario.objects.all()



    data = {
        'titulo': 'Inventario',
        'entity2': tablaInventario,
        'entity': tablaRetiro,
    }

    return render(request, "ControlAulasApp/inventario.html", data)


def inventario_retiro(request):
    data = {
        'form': RetiroInventarioForm,
    }

    if request.method == 'POST':
        formulario = RetiroInventarioForm(data=request.POST, files=request.FILES)
        variable = request.POST.get('producto')
        print("este es EL NOMBRE", variable)
        if formulario.is_valid():

            formulario.save()

            messages.success(request, "Se registro el retiro correctamente")
            # print("hola mundo", RetiroInventario.objects.get('producto'))
            # n = RetiroInventario.objects.get('nombrePersonal')[(ultimo-1):ultimo]
            n = RetiroInventario.objects.order_by('id').last()
            # print("hola mundo", n.producto)

            for b in Inventario.objects.all():

                if n.producto == b.nombreProducto:
                    # print("AQUI ESTA", b)
                    total = b.cantidadAlmacenada - n.cantidadUtilizada

                    update = Inventario.objects.values('cantidadAlmacenada').filter(id=b.id).update(
                        cantidadAlmacenada=total)
                    # print("PRODUCTO", b.nombreProducto)
                    formulario.save()

            return redirect(to="inventario")
        data["form"] = formulario

    return render(request, "ControlAulasApp/retiroInventario.html", data)


def aforoview(request):
    calculo = Aforo.objects.all()

    data = {
        'titulo': 'Aforo',
        'entity': calculo,
    }
    return render(request, 'ControlAulasApp/aforo.html', data)


def calcularAforo(request):
    data = {
        'form': AforoForm
    }

    if request.method == 'POST':
        formulario = AforoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")

            dato = Aforo.objects.order_by('id').last()

            # print("hola mundo", n.producto)
            c = dato.largoGeneral
            b = dato.largoDemarcacion
            columna = 0
            c -= 200
            while c > 0:

                if c >= b:
                    c = c - b
                    columna += 1
                c -= 100

            d = dato.anchoGeneral
            a = dato.anchoDemarcacion
            fila = 0
            while d > 0:

                if d >= a:
                    d = d - a
                    fila += 1
                d -= 150

            aforo = columna * fila + 1
            update = Aforo.objects.values('resultado').filter(id=dato.id).update(resultado=aforo)
            # print("PRODUCTO", b.nombreProducto)

            return redirect(to="aforo")
        data["form"] = formulario

    return render(request, "ControlAulasApp/calculoAforo.html", data)


def Admin(request):
    return render(request, "ControlAulasApp/admin.html")


def Detallepublicaciones(request, slug):
    publicacion = get_object_or_404(Publicacion, slug=slug)
    context = {'detalle_publicacion': publicacion}
    return render(request, "ControlAulasApp/Publicaciones.html", context)
