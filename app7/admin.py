from django.contrib import admin
from .models import Hospitalizacion
# Register your models here.
class HospitalizacionAdmin(admin.ModelAdmin):
    readonly_fields=("fecha_creacion",)
    
admin.site.register(Hospitalizacion,HospitalizacionAdmin)