from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]
