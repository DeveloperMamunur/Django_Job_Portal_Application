from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import Profile

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def dashboard(request):
    role = request.user.profile.role
    if role == 'employer':
        return redirect('employer_dashboard')
    else:
        return redirect('applicant_dashboard')

@login_required
def LogoutView(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('home')