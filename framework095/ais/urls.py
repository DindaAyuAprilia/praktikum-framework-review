from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import StudentsViewSet

# Membuat router DRF
router = DefaultRouter()
router.register(r'students', StudentsViewSet)  # Menyambungkan StudentsViewSet ke URL /students/

urlpatterns = [
    path('about', views.about, name="about"),
    path('', views.homepage),
    path('student/', views.student_index, name='student_index'),
    path('student/create/', views.student_create, name='student_create'),# Create
    path('student/update/<int:student_id>/', views.student_update, name='student_update'), # Updtae
    path('student/delete/<int:student_id>', views.student_delete, name='student_delete'), # Delete
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard/student/', views.dashboard_student, name='dashboard_student'),
    path('dashboard/teacher/', views.dashboard_teacher, name='dashboard_teacher'),
    path('api/', include(router.urls)), 

]