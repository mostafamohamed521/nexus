"""
services_app/models.py
Service and testimonial models.
"""
from django.db import models


class Service(models.Model):
    ICON_CHOICES = [
        ('rocket', 'Rocket'), ('shield', 'Shield'), ('chart', 'Chart'),
        ('code', 'Code'), ('cloud', 'Cloud'), ('star', 'Star'),
        ('bolt', 'Bolt'), ('eye', 'Eye'),
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='star')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Service'

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    avatar = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.company}"


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
