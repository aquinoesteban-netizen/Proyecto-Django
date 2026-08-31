from django.shortcuts import render
def inicio(request):
    """Vista para la página de inicio"""

    return render(request, 'portal/inicio.html')
def juegos(request):
    
    """Vista para el catálogo de juegos"""

    return render(request, 'portal/juegos.html')