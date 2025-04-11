from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/img/', null=True, blank=True)
    youtube_url = models.URLField(max_length=500, null=True, blank=True)
    # students = models.ManyToManyField(User, related_name="courses")  # Relación con los usuarios

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)




class Lesson(models.Model):
    # TEMPLATE_CHOICES = [
    #     ("template_1.html", "Diseño 1"),
    #     ("template_2.html", "Diseño 2"),
    #     ("template_3.html", "Diseño 3"),
    # ]

    title = models.CharField(max_length=255)
    content = models.TextField(default="")
    content_page = models.TextField(blank=True, null=True)  # Se agrega este campo
    course = models.ForeignKey("Course", on_delete=models.CASCADE, related_name="lessons")
    order = models.PositiveIntegerField(default=0)
    template = models.CharField(max_length=100, default="course/lessons/curso/leccion1.html", help_text="Ejemplo: course/lessons/curso/leccion1.html")

    video_url = models.URLField(blank=True, null=True)  # Nuevo atributo para el video
    # document = models.FileField(upload_to=lesson_file_path, blank=True, null=True)  # Para documentos
    # audio = models.FileField(upload_to=lesson_audio_path, blank=True, null=True)  # Para audios
    
    class Meta:
        ordering = ["course"]  # 🔹 Ordena por título A-Z

    def __str__(self):
        # return self.title
        return f"{self.course} - {self.order} - {self.title}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='clientes/logos/')
    pais = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre