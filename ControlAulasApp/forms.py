from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

from ControlAulasApp.models import Horario


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
