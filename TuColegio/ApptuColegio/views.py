from django.shortcuts import render
from .models import Colegios, Alumnos, Asignaturas
from .forms import ColegiosForm, AlumnosForm, AsignaturasForm



def agregar_colegios(request):
    
    if request.method == "POST":
        formulario = ColegiosForm(request.POST)

        if formulario.is_valid():
            info_dict = formulario.cleaned_data

            nuevo_colegio = Colegios(nombre = info_dict["nombre"],
                                     especialidad = info_dict["especialidad"],
                                     ubicacion = info_dict["ubicacion"],
                                     precio = info_dict["precio"],
                                     mail = info_dict["mail"])
            nuevo_colegio.save()

            return render(request, "ApptuColegio/buscar_colegio.html")
    
    else:
        formulario = ColegiosForm()

    return render(request, "ApptuColegio/nuevo_colegio.html", {"form":formulario})

def agregar_alumnos(request):
    
    if request.method == "POST":
        formulario = AlumnosForm(request.POST)

        if formulario.is_valid():
            info_dict = formulario.cleaned_data

            nuevo_alumno = Alumnos(nombre = info_dict["nombre"],
                                     edad = info_dict["edad"],
                                     promedio = info_dict["promedio"])
            
            nuevo_alumno.save()

            return render(request, "ApptuColegio/buscar_colegio.html")
    
    else:
        formulario = AlumnosForm()

    return render(request, "ApptuColegio/nuevo_alumno.html", {"form":formulario})

def agregar_asignaturas(request):
    
    if request.method == "POST":
        formulario = AsignaturasForm(request.POST)

        if formulario.is_valid():
            info_dict = formulario.cleaned_data

            nueva_asignatura = Asignaturas(nombre = info_dict["nombre"],
                                     cargaHoraria = info_dict["cargaHoraria"],
                                     examenes = info_dict["examenes"])
            
            nueva_asignatura.save()

            return render(request, "ApptuColegio/buscar_colegio.html")
    
    else:
        formulario = AsignaturasForm()

    return render(request, "ApptuColegio/nueva_asignatura.html", {"form":formulario})

def buscar_colegio(request):
    return render(request, "ApptuColegio/buscar_colegio.html")

def resultados_colegio(request):
    colegio = request.GET["nombre_colegio"]
    resultados = Colegios.objects.filter(nombre__icontains=colegio)

    return render(request, "ApptuColegio/resultados.html", {"resultados":resultados})