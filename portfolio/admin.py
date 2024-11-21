# portfolio/admin.py
from django.contrib import admin
from .models import PortfolioItem

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'client_name', 'developer_name', 'created_at')
    search_fields = ('title', 'client_name', 'developer_name')
