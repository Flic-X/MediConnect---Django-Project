from datetime import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentForm
from django.utils import timezone

@login_required
def doctor_dashboard(request):
    appointments = Appointment.objects.filter(doctor=request.user).order_by('date')
    context = {
        'appointments': appointments,
        'doctor': request.user
    }
    return render(request, 'appointments/doctor_dashboard.html', context)

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect('patient_dashboard')  # make sure this URL name exists
    else:
        form = AppointmentForm()
    return render(request, 'appointments/book_appointment.html', {'form': form})


def patient_dashboard(request):
    patient = request.user

    upcoming_appointments = Appointment.objects.filter(patient=patient, date__gte=timezone.now().date()).order_by('date','time')
    past_appointments = Appointment.objects.filter(patient=patient, date__lt=timezone.now().date()).order_by('-date','-time')

    return render(request, 'appointments/patient_dashboard.html', {
        'upcoming_appointments': upcoming_appointments,
        'past_appointments': past_appointments
    })

def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient=request.user)

    if appointment.status == 'booked':
        appointment.status = 'cancelled'
        appointment.save()

    return redirect('patient_dashbaord')

def mark_appointment_completed(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, doctor=request.user)
    if appointment.status == 'booked':
        appointment.status = 'completed'
        appointment.save()
    return redirect('doctor_dashboard')