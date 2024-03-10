from django.forms import ModelForm
from .models import Hospitalizacion

class HospitalizacionForm(ModelForm):
    class Meta:
        model=Hospitalizacion
        fields=[
            'id_hospitalizacion',
            'nombre_paciente',
            'edad',
            'pais_origen',
            'idioma',
            'check_in',
            'check_out',
            'no_visitas'
        ]