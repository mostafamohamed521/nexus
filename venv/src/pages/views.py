"""
pages/views.py
Static and dynamic page views: Home, About, Services overview, Dashboard redirect.
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from services_app.models import Service, Testimonial, TeamMember
from contacts.models import ContactMessage


def home_view(request):
    featured_services = Service.objects.filter(is_featured=True)[:6]
    testimonials = Testimonial.objects.filter(is_active=True)[:6]
    return render(request, 'pages/home.html', {
        'featured_services': featured_services,
        'testimonials': testimonials,
        'page_title': 'Home',
    })


def about_view(request):
    team = TeamMember.objects.all()
    return render(request, 'pages/about.html', {
        'team': team,
        'page_title': 'About Us',
    })


def dashboard_redirect(request):
    from django.shortcuts import redirect
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)


def error_500(request):
    return render(request, 'errors/500.html', status=500)
