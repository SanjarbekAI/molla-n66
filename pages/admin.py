from django.contrib import admin

from pages.models import ContactModel, StoreModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'created_at']
    list_filter = ['created_at', 'is_read']
    search_fields = ['name', 'email', 'message']
    ordering = ['-created_at']


@admin.register(StoreModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'created_at']
    list_filter = ['created_at', 'picked']
    search_fields = ['name', 'address']
    ordering = ['-created_at']
