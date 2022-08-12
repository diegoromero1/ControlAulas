import self as self
from django import forms

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from ControlAulasApp.models import Horario, RegistroIncidencia, RetiroInventario, Inventario, Aforo
from django.core.exceptions import ValidationError


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Ingrese su contraseña actual'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Ingrese nueva contraseña '}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Repita la contraseña '}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ["observacion"]


class RegistroIncidenciaForm(forms.ModelForm):
    class Meta:
        model = RegistroIncidencia
        fields = ["nombreAfectado"]


class AgregarIncidenciaForm(forms.ModelForm):
    class Meta:
        model = RegistroIncidencia
        fields = '__all__'


class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = '__all__'


# class DateTimeInput(forms.DateTimeInput):
#     input_type = 'date'


class RetiroInventarioForm(forms.ModelForm):
    # fecha = forms.DateField(widget=widgets.AdminDateWidget(format="%Y/%m/%d"))
    fecha = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format="%d/%m/%Y"))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))

    # producto = forms.ModelChoiceField(queryset=Inventario.objects.all(),
    #                                   widget=forms.Select(attrs={'class': 'form-control'}), )

    def clean_producto(self):
        # cantidad = self.cleaned_data.get('cantidadUtilizada')
        produc = self.cleaned_data.get('producto')
        var = 'inicial'
        # cantidadinv = 100
        for b in Inventario.objects.all():
            print("AQUI ESTA", b)
            if produc == b.nombreProducto:
                var = b.nombreProducto
                # cantidadinv = b.cantidadAlmacenada
                print("Escogida AQUI", var)

        if produc != var:
            print("AQUI ESTA la otra", var)
            raise forms.ValidationError('nombre no valido')
        return produc

    def clean_cantidadUtilizada(self):
        produc = self.cleaned_data.get('producto')
        cantidad = self.cleaned_data.get('cantidadUtilizada')
        var = 'inicial'
        cantidadinv = 1
        for b in Inventario.objects.all():

            print("AQUI ESTA", b)
            if produc == b.nombreProducto:
                var = b.nombreProducto
                cantidadinv = b.cantidadAlmacenada

        print("Escogida AQUI", produc)
        if cantidad > cantidadinv:
            print("AQUI ESTA la otra", cantidadinv)
            raise forms.ValidationError('Stock no valido')
        return cantidad

    class Meta:
        model = RetiroInventario
        fields = ["nombrePersonal", "apellidosPersonal", 'fecha', 'hora', "producto", "cantidadUtilizada",
                  ]
        # widgets = {
        #
        #     'fecha': DateTimeInput(attrs={'class': 'form-control'}),
        #
        # }


class AforoForm(forms.ModelForm):
    class Meta:
        model = Aforo
        fields = ["nombre","largoGeneral","anchoGeneral","largoDemarcacion","anchoDemarcacion"]
