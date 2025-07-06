from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

class Appointment(models.Model):
    doctor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointments_as_doctor')
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='appointments_as_patient')
    date = models.DateTimeField(default=timezone.now)
    symptoms = models.TextField()

    def __str__(self):
        return f"Appointment on {self.date.strftime('%Y-%m-%d %H:%M')} - Dr. {self.doctor.username} with {self.patient.username}"
    
