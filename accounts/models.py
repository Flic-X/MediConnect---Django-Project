
from django.contrib.auth.models import AbstractUser
from django.db import models

USER_TYPES =(
    ('doctor', 'Doctor'),
    ('patient', 'Patient')
)

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPES)

    age = models.PositiveBigIntegerField(null=True, blank=True)
    specialization = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.user_type})"

