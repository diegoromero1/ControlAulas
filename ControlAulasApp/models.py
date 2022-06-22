from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.utils.html import format_html


class EstadoAula(models.Model):
    nombreSala = models.CharField(max_length=40, verbose_name="nombre de sala")
    estado = models.CharField(max_length=20, blank=False)
    aforo = models.CharField('Aforo',max_length=30, blank=True)
    sector = models.CharField('Sector',max_length=30, blank=True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombreSala, self.estado)

    def Estado_Salas(self):
        if self.estado.upper() == 'habilitada'.upper():
            return format_html('<span style="color: green;">{0}</span>'.format(self.estado))
        if self.estado.upper() == 'en curso'.upper():
            return format_html('<span style="color: blue;">{0}</span>'.format(self.estado))
        if self.estado.upper() == 'sin desinfeccion'.upper():
            return format_html('<span style="color: red;">{0}</span>'.format(self.estado))


class Horario(models.Model):
    nombrePersonal = models.CharField(max_length=20, verbose_name="nombre del personal")
    apellidosPersonal = models.CharField(max_length=20, verbose_name="apellidos del personal")
    asignacion = models.CharField(max_length=40, verbose_name="asignacion sala")
    hora = models.CharField(max_length=20, verbose_name="hora")
    dia = models.CharField(max_length=20, verbose_name="dia")
    observacion = models.TextField(blank=True, null=True, verbose_name="observacion detectada")

    def nombre_completo(self):
        return "{} {}".format(self.nombrePersonal, self.apellidosPersonal)

    def __str__(self):
        # texto = "{0} ({1})"
        # return texto.format(self.nombre_completo, self.asignacion) # para que el segundo dato aparesca en parentesis
        return self.nombre_completo()


class Publicacion(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=90, blank=False, null=False)
    slug = models.SlugField('Slug', max_length=255, unique=True)
    contenido = RichTextField('Contenido')
    descripcion = models.CharField('Descripcion', max_length=200, blank=False, null=False)
    estado = models.BooleanField('Categoria Activada/Categoria Desactivada', default=True)
    imagen = models.ImageField(upload_to="img", blank=True, null=True)
    imagen2 = models.ImageField(upload_to="img",blank=True, null=True)


    def save(self, *args, **kwargs):
        self.url = slugify(self.titulo)
        super(Publicacion, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return self.titulo


class Archivo(models.Model):
    adminupload = models.FileField('Archivo', upload_to='descarga')
    descripcion = models.CharField('Descripcion', max_length=200, blank=False, null=False)
    titulo = models.CharField('Titulo', max_length=90, blank=False, null=False)

    def __str__(self):
        return self.titulo
