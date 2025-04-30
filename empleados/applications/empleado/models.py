from django.db import models
from applications.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField('habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades del empleado'
        ordering = ['habilidad']
        unique_together = ('habilidad',)

    def __str__(self):
        return self.habilidad 

class Empleado (models.Model):


    JOB_CHOICES =(
        ('0', 'Contador'),
        ('1', 'Administrativo'),
        ('2', 'Desarrollador'),
        ('3', 'Analista Funcional'),
        ('4', 'Otro'),
    )

    nombre = models.CharField('Nombre', max_length=60)
    apellido = models.CharField('Apellido', max_length=60)
    trabajo = models.CharField('Puesto', max_length=1, choices= JOB_CHOICES)
    Departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)
    Habilidades= models.ManyToManyField(Habilidades)

    def __str__(self):
        return self.nombre + ' - ' + self.apellido 