from django.db import models
from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField

# Create your models here.

class Habilidades(models.Model):
    habilidad= models.CharField('Habilidad', max_length=50)

    class meta:
        verbose_name='Habilidad'
        verbose_name_plural='Habilidades Empleado'

    def __str__(self):
        return str(self.id)+'-'+self.habilidad

class Empleado(models.Model):
    """ Modelo para tabla empleado"""

    JOB_CHOICES=(
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),
    )
    first_name= models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=50)
    full_name= models.CharField('Nombres completos', max_length=120, blank=True)
    job=models.CharField('Trabajo',max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar= models.ImageField( upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida=RichTextField()

    def __str__(self):
        return str(self.id)+'-'+self.first_name+'-'+self.last_name