from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Appointment


@login_required
def doctor_dashboard(request):
    return render(request, 'appointments/doctor_dashboard.html')

    
    appointments = Appointment.objects.filter(doctor=request.user).order_by('date')


    context = {
        'appointments': appointments,
        'doctor': request.user
    }

    return render(request, 'appointments/doctor_dashboard.html', context)

