# app_name/admin.py

from django.contrib import admin
from .models import CustomUser, File, DownloadLink

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_ops_user', 'is_client_user')
    list_filter = ('is_ops_user', 'is_client_user')
    search_fields = ('username', 'email')

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('file', 'user', 'uploaded_at')
    list_filter = ('uploaded_at', 'user')
    search_fields = ('file__name', 'user__username')

@admin.register(DownloadLink)
class DownloadLinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'file', 'created_at', 'is_active')
    list_filter = ('created_at', 'is_active')
    search_fields = ('link', 'file__file__name')
