from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from course.models import Enrollment, Course


def home_redirect(request):
    return redirect("dashboard")  # Asegúrate de que "dashboard" existe en las URLs registradas

def user_login(request):
    """Vista para iniciar sesión con username y password"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("accounts:dashboard")  # Redirige al dashboard después de iniciar sesión
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "accounts/login.html")

@login_required
def dashboard(request):
    """Muestra los cursos en los que el usuario está inscrito"""
    user_courses = Enrollment.objects.filter(user=request.user).select_related('course')
    
    # 🛠️ Debugging: Verifica si hay cursos
    print(f"Usuario autenticado: {request.user}")
    print(f"Cursos matriculados: {user_courses}")

    return render(request, "accounts/dashboard.html", {"user_courses": user_courses})


@login_required
def user_courses(request, course_id):
    """Muestra la página de un curso si el usuario está inscrito"""
    enrollment = Enrollment.objects.filter(user=request.user, course_id=course_id).first()

    if not enrollment:
        messages.error(request, "No tienes acceso a este curso")
        return render(request, "accounts/no_access.html")  

    return render(request, "accounts/courses.html", {"course": enrollment.course})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'course/course_detail.html', {'course': course})