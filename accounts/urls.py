from django.urls import path
from .views import user_login, dashboard, user_courses, course_detail
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts"  # Para usar en templates con {% url 'accounts:login' %}

urlpatterns = [
    # Vista de Login con el template personalizado
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    
    # Dashboard (requiere login)
    path("dashboard/", dashboard, name="dashboard"),

    # Logout con redirección al login
    path("accounts/logout/", LogoutView.as_view(), name="logout"),

     
    path("course/<int:course_id>/", user_courses, name="user_courses"),
    
  

]
