from django import forms


class ColegiosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    especialidad = forms.CharField(max_length=50)
    ubicacion = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=20, decimal_places=2)
    mail = forms.EmailField(max_length=100)


    
class AlumnosForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    promedio = forms.DecimalField(max_digits=4, decimal_places=2)

    
class AsignaturasForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    cargaHoraria = forms.IntegerField()
    examenes = forms.IntegerField()

