from django.shortcuts import redirect, render
from course.models import Cliente  # Asegúrate de importar el modelo

# def home_redirect(request):
#     # return redirect('course:list')  # Redirige a la página principal que desees
    
#     return redirect('accounts:login')  # Redirige a la página principal que desees

def home(request):
    clientes = Cliente.objects.all()
    return render(request, 'home.html', {'clientes': clientes})