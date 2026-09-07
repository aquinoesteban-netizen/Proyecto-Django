from django.shortcuts import render
def inicio(request):
    """Vista para la página de inicio"""
    return render(request, 'portal/inicio.html')

def placas(request): 
    """Vista para los tipos de placas Arduino""" 
    return render(request, 'portal/placas.html')
