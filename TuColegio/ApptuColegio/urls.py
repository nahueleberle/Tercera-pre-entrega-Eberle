from django.urls import path
from ApptuColegio import views

urlpatterns = [
    path("nuevo_colegio/", views.agregar_colegios),
    path("nuevo_alumno/", views.agregar_alumnos),
    path("nueva_asignatura/", views.agregar_asignaturas),
    path("buscar_colegio/", views.buscar_colegio),
    path("resultados/", views.resultados_colegio),
]