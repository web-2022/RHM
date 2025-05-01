from django.contrib import admin
from .models import Course, Enrollment, Lesson, Cliente, ArchivoAdjunto

# Register your models here.
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Lesson)
admin.site.register(Cliente)
admin.site.register(ArchivoAdjunto)