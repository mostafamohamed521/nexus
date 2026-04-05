from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .forms import ContactForm


@require_http_methods(["GET", "POST"])
def contact_view(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            contact = form.save(commit=False)
            contact.ip_address = request.META.get('REMOTE_ADDR')
            contact.save()
            messages.success(request, "Message sent! We'll get back to you within 24 hours.")
            return redirect('contact')
        else:
            messages.error(request, 'Please fix the errors below.')

    return render(request, 'contacts/contact.html', {
        'form': form,
        'page_title': 'Contact Us',
    })
