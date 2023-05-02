# registro/views.py

from django.shortcuts import render
from .forms import AlumnoForm, ProfesorForm

def insertar(request):
    if request.method == 'POST':
        # Si se envió el formulario, procesarlo
        form_alumno = AlumnoForm(request.POST)
        form_profesor = ProfesorForm(request.POST)

        if form_alumno.is_valid():
            form_alumno.save()
        elif form_profesor.is_valid():
            form_profesor.save()

    # Mostrar el formulario de inserción
    form_alumno = AlumnoForm()
    form_profesor = ProfesorForm()

    context = {
        'form_alumno': form_alumno,
        'form_profesor': form_profesor,
    }
    return render(request, 'registro/insertar.html', context)
