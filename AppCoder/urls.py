from django.contrib import admin
from django.urls import path

from .views import (
    cursos,
    inicio,
    cursos_crud_read_view,
    profesor,
    profesores_crud_read_view,
    profesores_crud_delete_view,
    profesores_crud_update_view,
    # CBV
    CursoCreateView,
    CursoDetail,
    CursoDeleteView,
    CursoListView,
    CursoUpdateView,
    # Login
    login_view,
    editar_usuario_view,
    registro_view,
    CambiarContrasenia
)

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", inicio),
    path("inicio/", inicio),
    path("cursos/", cursos),
    path("cursos_lista/", cursos_crud_read_view),
    path("profesores/", profesor),
    path("profesores_lista/", profesores_crud_read_view),
    path("profesores-eliminar/<profesor_email>/", profesores_crud_delete_view),
    path("profesores-editar/<profesor_email>/", profesores_crud_update_view),

    ### CBV

    path("curso/list", CursoListView.as_view(), name="curso-list"),
    path("curso/new", CursoCreateView.as_view(), name="curso-create"),
    path("curso/<pk>", CursoDetail.as_view(), name="curso-detail"),
    path("curso/<pk>/update", CursoUpdateView.as_view(), name="curso-update"),
    path("curso/<pk>/delete", CursoDeleteView.as_view(), name="curso-delete"),

    ### Login / Logout
    path("registro", registro_view, name="registro"),
    path("login", login_view, name="login"),

    path("logout", LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),

    # Edicion de usuario
    path("editar-usuario", editar_usuario_view, name="editar-usuario"),
    # path("cambiar-contrasenia", CambiarContrasenia.as_view(), name="cambiar-contrasenia")

]