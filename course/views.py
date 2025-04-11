from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Lesson
from course.models import Enrollment

@login_required
def course_list(request):
    """Muestra la lista de cursos en los que está matriculado el usuario."""
    user = request.user
    courses = Course.objects.filter(enrollment__user=user)
    return render(request, "course/course_list.html", {"courses": courses})

@login_required
def course_detail(request, course_id, lesson_id=None):
    """Muestra el curso con el índice de lecciones y el contenido de la lección seleccionada."""
    course = get_object_or_404(Course, id=course_id)
    # Verifica que el usuario esté inscrito en el curso
    if not Enrollment.objects.filter(user=request.user, course=course).exists():
        return render(request, "course/access_denied.html")  # O redirige a una página de acceso denegado

    lessons = course.lessons.order_by("order")

    # Determina la lección a mostrar
    lesson = lessons.first() if lesson_id is None else get_object_or_404(Lesson, id=lesson_id, course=course)

    return render(request, "course/course_detail.html", {
        "course": course,
        "lessons": lessons,
        "lesson": lesson,
    })

    

def lesson_detail(request, course_id, lesson_id):
    course = get_object_or_404(Course, id=course_id)
    # Verifica que el usuario esté inscrito en el curso
    if not Enrollment.objects.filter(user=request.user, course=course).exists():
        return render(request, "course/access_denied.html")  # O redirige a una página de acceso denegado

    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
    lessons = course.lessons.order_by("order")

    return render(request, lesson.template, {
        "course": course,
        "lesson": lesson,
        "lessons": lessons,
    })
