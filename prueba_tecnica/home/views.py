from django.shortcuts import render
from .forms import CabidaForm


def calcular_cabida(request):
    resultado = None
    if request.method == 'POST':
        form = CabidaForm(request.POST)
        if form.is_valid():
            cabida = form.save(commit=False)
            cabida.calcular_cabida()
            cabida.save()
            resultado = cabida.resultado
    else:
        form = CabidaForm()

    return render(request, 'cabida_form.html', {'form': form, 'resultado': resultado})
