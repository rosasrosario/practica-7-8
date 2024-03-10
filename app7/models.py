from django.db import models
from django.contrib.auth.models import User

# Create your models here.
OPCIONES_IDIOMA = [
    ('es', 'Español'),
    ('en', 'English'),
]

class Hospitalizacion(models.Model):
    id_hospitalizacion = models.IntegerField()
    nombre_paciente = models.CharField(max_length=512)
    edad = models.IntegerField()
    motivo = models.CharField(max_length=512)
    pais_origen = models.CharField(max_length=512)
    idioma = models.CharField(max_length=512, choices = OPCIONES_IDIOMA)
    check_in = models.DateField()
    check_out = models.DateField()
    no_visitas = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return f'{self.nombre_paciente} - {self.motivo} - {self.no_visitas} visitas'
    