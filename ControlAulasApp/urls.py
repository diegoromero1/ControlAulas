from django.contrib import admin
# from django.contrib.auth.views import login

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordChangeView
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from ControlAulasApp import views
from ControlAulasApp.views import IndexView, Estados, Detallepublicaciones, \
    PasswordsChangeView, edicion_tabla, Horarios, descarga, RegistroIncidencias, edicion_tabla_incidencias, \
    agregarIncidencia, Inventarios, inventario_retiro, aforoview,calcularAforo

urlpatterns = [
    path('inicio/', IndexView, name='index'),
    # path('',login, {'template_name':'login.html'}, name='login'),
    path('', LoginView.as_view(template_name='ControlAulasApp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='ControlAulasApp/logout.html'), name='logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_complete'),

    path('estados/', Estados, name='estados'),
    path('horario/', Horarios, name='horario'),
    path('incidencias/', RegistroIncidencias, name='incidencias'),
    path('inventario/', Inventarios, name='inventario'),
    path('aforo/', aforoview, name='aforo'),

    # path('registrarObservacion/', registrar_observacion),
    path('edicionTabla/<id>/', edicion_tabla, name="edicionTabla"),
    path('edicionTablaIncidencia/<id>/', edicion_tabla_incidencias, name="edicionTablaIncidencia"),
    path('agregarIncidencia/', agregarIncidencia, name='agregarIncidencia'),
    path('calculoAforo/', calcularAforo, name='calculoAforo'),

    path('retiroInventario/', inventario_retiro, name='retiroInventario'),

    path('password/', PasswordsChangeView.as_view(template_name='accounts/change_password.html'),
         name='password'),
    path('password_success/', views.password_success, name="password_success"),

    path('descarga/', descarga, name="descarga"),

    path('admin/', views.Admin, name="admin"),

    path('<str:slug>/', Detallepublicaciones, name="Detalle_publicaciones"),

]
