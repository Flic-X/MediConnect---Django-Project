from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

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
