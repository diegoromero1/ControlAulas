# Generated by Django 3.2.9 on 2022-08-02 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControlAulasApp', '0011_alter_horario_dia'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroIncidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreAfectado', models.CharField(max_length=20, verbose_name='nombre del afectado')),
                ('apellidosAfectado', models.CharField(max_length=20, verbose_name='apellidos del afectado')),
                ('nombreRegistrante', models.CharField(max_length=20, verbose_name='nombre del registrante')),
                ('apellidosRegistrante', models.CharField(max_length=20, verbose_name='apellidos del registrante')),
                ('nombreSala', models.CharField(max_length=40, verbose_name='nombre de sala')),
                ('fecha', models.DateField(null=True, verbose_name='Fecha')),
                ('descripcionCaso', models.TextField(blank=True, null=True, verbose_name='Descripcion del caso')),
            ],
        ),
    ]
