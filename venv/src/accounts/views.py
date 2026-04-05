"""
accounts/views.py
Authentication views: register, login, logout, dashboard, profile.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm, LoginForm, ProfileUpdateForm
from contacts.models import ContactMessage
from services_app.models import Service


@require_http_methods(["GET", "POST"])
def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome aboard, {user.first_name or user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')
    return render(request, 'accounts/register.html', {'form': form})


@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            return redirect(request.GET.get('next', 'dashboard'))
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been signed out.')
    return redirect('home')


@login_required
def dashboard_view(request):
    recent_contacts = ContactMessage.objects.filter(email=request.user.email).order_by('-created_at')[:5]
    services_count = Service.objects.count()
    context = {
        'recent_contacts': recent_contacts,
        'services_count': services_count,
        'messages_count': recent_contacts.count(),
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def profile_view(request):
    form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    return render(request, 'accounts/profile.html', {'form': form})
