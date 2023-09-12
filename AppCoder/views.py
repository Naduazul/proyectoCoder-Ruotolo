from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import citasFormulario, profesionalesFormulario
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy

def inicio (request):
    return render(request, 'AppCoder/inicio.html')

def especialidad (request):
    return render(request, 'AppCoder/especialidad.html')

#def profesionales (request):
  #  return render(request, 'AppCoder/profesionales.html')

def pacientes (request):
    return render(request, 'AppCoder/pacientes.html')

#def citas (request):
    #return render(request, 'AppCoder/citas.html')



def citas(request):
    if request.method == "GET":
        print("+" * 90) #  Imprimimos esto para ver por consola
        print("+" * 90) #  Imprimimos esto para ver por consola
        return render(
            request,
            "AppCoder/citas_formulario_avanzado.html",
            {"form": citasFormulario()}
        )
    else:
        print("*" * 90)     #  Imprimimos esto para ver por consola
        print(request.POST) #  Imprimimos esto para ver por consola
        print("*" * 90)     #  Imprimimos esto para ver por consola

        modelo = Citas(nombre=request.POST["nombre"], codigo=request.POST["codigo turno"])
        modelo.save()
        return render(
            request,
            "AppCoder/inicio.html",
        )


def citas_crud_read_view(request):
    citas = Citas.objects.all()
    return render(request, "AppCoder/citas-lista.html", {"citas": citas})


def profesionales(request):
    if request.method == "GET":
        return render(
            request,
            "AppCoder/profesionales_formulario_avanzado.html",
            {"form": profesionalesFormulario()}
        )
    else:
        formulario = profesionalesFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Profesionales(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                email=informacion["email"],
                cargo=informacion["cargo"]
            )
            modelo.save()
        return render(
            request,
            "AppCoder/inicio.html",
        )

def profesionales_crud_read_view(request):
    profesional = Profesionales.objects.all()
    return render(request, "AppCoder/profesionales-lista.html", {"profesional": profesional})


def profesionales_crud_delete_view(request, profesional_email):
    profesional_a_eliminar = Profesionales.objects.filter(email=profesional_email).first()
    profesional_a_eliminar.delete()
    return profesionales_crud_read_view(request)


def profesionales_crud_update_view(request, profesional_email):
    profesional = Profesionales.objects.filter(email=profesional_email).first()
    if request.method == "GET":
        formulario = profesionalesFormulario(
            initial={
                "nombre": profesional.nombre,
                "apellido": profesional.apellido,
                "email": profesional.email,
                "profesion": profesional.cargo
            }
        )
        return render(request, "AppCoder/profesionales_formulario_edicion.html", {"form": formulario, "profesional": profesional})
    else:
        formulario = profesionalesFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            profesional.nombre=informacion["nombre"]
            profesional.apellido=informacion["apellido"]
            profesional.email=informacion["email"]
            profesional.cargo=informacion["cargo"]
            profesional.save()
        return profesionales_crud_read_view(request)



####################  ClassBasedViews (CBV)  - Vistas basadas en Clases #########################################

class citasListView(ListView):
    model = Citas
    context_object_name = "citas"
    template_name = "AppCoder/cbv_citas_list.html"


class citasDetail(DetailView):
    model = Citas
    template_name = "AppCoder/cbv_citas_detail.html"


class citasCreateView(CreateView):
    model = Citas
    template_name = "AppCoder/cbv_citas_create.html"
    success_url = reverse_lazy("citas-list")
    fields = ["citas", "turno_tomado"]


class citasUpdateView(UpdateView):
    model = Citas
    template_name = "AppCoder/cbv_citas_update.html"
    success_url = reverse_lazy("citas-list")
    fields = ["citas"]

class citasDeleteView(DeleteView):
    model = Citas
    template_name = "AppCoder/cbv_citas_delete.html"
    success_url = reverse_lazy("citas-list")