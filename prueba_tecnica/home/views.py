from django.shortcuts import render
from .forms import CabidaForm
from .utils import calcular_cabida

def calcular_view(request):
    resultado = None  # Para almacenar el resultado del cálculo

    if request.method == 'POST':
        form = CabidaForm(request.POST)
        if form.is_valid():
            # Obtener los valores del formulario
            x = form.cleaned_data['x']
            y = form.cleaned_data['y']
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']

            # Usar la función para calcular la cabida
            resultado = calcular_cabida(x, y, a, b)
    else:
        form = CabidaForm()

    # Renderizar la plantilla con el formulario y el resultado
    return render(request, 'cabida_form.html', {'form': form, 'resultado': resultado})
