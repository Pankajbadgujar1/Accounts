from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name= 'register_student'),
    path('login/', views.login, name= 'login_student'),
    path('HomePage/', views.home, name= 'teachers_home'),
]
