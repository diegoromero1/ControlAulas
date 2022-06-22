# Create your views here.
import os

from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView

from ControlAulas import settings
from ControlAulasApp.forms import PasswordChangingForm, HorarioForm
from ControlAulasApp.models import EstadoAula, Horario, Publicacion, Archivo
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.core.paginator import Paginator


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

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(tablaEstados, 4)
        tablaEstados = paginator.page(page)
    except:
        raise Http404

    data = {
        'titulo': 'Estado de salas',
        'entity': tablaEstados,
        'paginator': paginator
    }
    # return render(request, "ControlAulasApp/estadoaulas.html",{"estados": tablaEstados})
    return render(request, "ControlAulasApp/estadoaulas.html", data)


def Horarios(request):
    tablaHorarios = Horario.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(tablaHorarios, 4)
        tablaHorarios = paginator.page(page)
    except:
        raise Http404

    data = {
        'titulo': 'Horario de desinfeccion',
        'entity': tablaHorarios,
        'paginator': paginator
    }

    return render(request, "ControlAulasApp/horario.html", data)


class HorariosListView(ListView):
    model = Horario
    template_name = 'ControlAulasApp/horario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Horario de desinfeccion'
        return context


# def Detallepublicaciones(request, slug):
#     publicacion = Publicacion.objects.all()
#     return render(request, "ControlAulasApp/Publicaciones.html", {'detalle_publicacion': publicacion})


# def registrar_observacion(request):
#     observacion = request.POST['txtObservacion']
#     horario = Horario.objects.create(observacion=observacion)
#     return redirect('ControAulasApp/horario.html')


def edicion_tabla(request, id):
    horario = get_object_or_404(Horario, id=id)

    data = {
        'form': HorarioForm(instance=horario)
    }

    if request.method == 'POST':
        formulario = HorarioForm(data=request.POST, instance=horario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado ccrrectamente")
            return redirect(to="horario")
        data["form"] = formulario

    return render(request, "ControlAulasApp/edicionTabla.html", data)


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
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(archivo, 4)
        archivo = paginator.page(page)
    except:
        raise Http404

    context = {
        'entity': archivo,
        'paginator': paginator

    }
    return render(request, 'ControlAulasApp/descarga.html', context)


def Detallepublicaciones(request, slug):
    publicacion = get_object_or_404(Publicacion, slug=slug)
    context = {'detalle_publicacion': publicacion}
    return render(request, "ControlAulasApp/Publicaciones.html", context)
