from django.contrib import admin
from AppCoder import models
from .models import Citas
# Register your models here.

#admin.site.register(models.especialidad)
#admin.site.register(models.profesionales)
#admin.site.register(models.citas)
#admin.site.register(models.pacientes)
#admin.site.register(models.citas_Formulario)
#admin.site.register(models.inicio)





@admin.register(Citas)
class citasAdmin(admin.ModelAdmin):
    pass