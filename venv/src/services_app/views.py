from django.shortcuts import render, get_object_or_404
from .models import Service, Testimonial, TeamMember


def services_list(request):
    services = Service.objects.all()
    return render(request, 'services_app/list.html', {
        'services': services,
        'page_title': 'Our Services',
    })


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    related = Service.objects.exclude(pk=service.pk)[:3]
    return render(request, 'services_app/detail.html', {
        'service': service,
        'related': related,
    })
