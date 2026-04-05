from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'created_at')
    list_filter = ('status',)
    list_editable = ('status',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('ip_address', 'created_at')
    date_hierarchy = 'created_at'
