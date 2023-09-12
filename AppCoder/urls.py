
from django.urls import path
from django.http import HttpResponse
from AppCoder import views
from django.contrib import admin
from .views import *
from django.urls import path

from .views import (
    citas,
    inicio,
    citas_crud_read_view,
    profesionales,
    profesionales_crud_read_view,
    profesionales_crud_delete_view,
    profesionales_crud_update_view,
    # CBV
    citasCreateView,
    citasDetail,
    citasDeleteView,
    citasListView,
    citasUpdateView
)


urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path('citas_Formulario/', views.citas_Formulario, name='citas_Formulario'),
    path('citas/', views.citas, name='citas'),
    path('especialidad/', views.especialidad, name='especialidad'),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('profesionales/', views.profesionales, name='profesionales'),
    path("citas-lista/", citas_crud_read_view),
    path("profesionales/", profesionales),
    path("profesionales-lista/", profesionales_crud_read_view),
    path("profesionales-eliminar/<profesional_email>/", profesionales_crud_delete_view),
    path("profesionales-editar/<profesional_email>/", profesionales_crud_update_view),
    

    ### CBV

    path("citas/list", citasListView.as_view(), name="citas-list"),
    path("citas/new", citasCreateView.as_view(), name="citas-create"),
    path("citas/<pk>", citasDetail.as_view(), name="citas-detail"),
    path("citas/<pk>/update", citasUpdateView.as_view(), name="citas-update"),
    path("citas/<pk>/delete", citasDeleteView.as_view(), name="citas-delete"),

    
    ]
    





    



