from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, DoctorProfileForm, PatientProfileForm

def register_view(request):
    print("REGISTER VIEW CALLED ✅")  # DEBUG
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def dashboard_view(request):
    if request.user.user_type == 'doctor':
        return render(request, 'accounts/doctor_dashboard.html')
    elif request.user.user_type == 'patient':
        return render(request, 'accounts/patient_dashboard.html')
    else:
        return redirect('login')
    
@login_required
def profile_view(request):
    user = request.user
    if user.user_type == 'doctor':
        form_class = DoctorProfileForm
    else:
        form_class = PatientProfileForm

    if request.method == 'POST':
        form = form_class(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('dashboard')
    else:
        form = form_class(instance=user)

    return render(request, 'accounts/profile.html', {'form': form})
