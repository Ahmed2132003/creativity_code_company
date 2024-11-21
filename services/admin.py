from django.contrib import admin
from .models import Service, ServiceRequest

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'duration')

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('service', 'name', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('name', 'email', 'phone_number')
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_read')  # الحقول التي تظهر في قائمة الإشعارات
    list_filter = ('is_read', 'created_at')  # فلاتر جانبية
    search_fields = ('user__username', 'message')  # حقل البحث
    ordering = ('-created_at',)  # ترتيب الإشعارات