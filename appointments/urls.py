from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient/dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('mark_completed/<int:appointment_id>', views.mark_appointment_completed, name='mark_appointment_completed'),
    path('update-status/<int:appointment_id>', views.update_appointment_status, name='update_appointment_status'),
    path('appointment/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),

]
