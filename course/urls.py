from django.urls import path
from .views import course_list, course_detail, lesson_detail

app_name = "course"  # Nombre correcto de la app

urlpatterns = [
    path("", course_list, name="list"),  # Lista de cursos matriculados
    path("<int:course_id>/", course_detail, name="course_detail"),  # Página del curso
    # path("<int:course_id>/lesson/<int:lesson_id>/", lesson_detail, name="lesson_detail"),  # Página de una lección específica
    
    path("<int:course_id>/lesson/<int:lesson_id>/", lesson_detail, name="lesson_detail"),
    

    
]


