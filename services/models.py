from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='service_images/')
    video = models.FileField(upload_to='service_videos/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=255)

    def __str__(self):
        return self.title

from django.db import models
from django.conf import settings  # استيراد الإعدادات

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('under_review', 'قيد المراجعة'),
        ('approved', 'تمت الموافقة'),
        ('in_progress', 'تتم البرمجة الآن'),
        ('completed', 'انتهت'),
    ]

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='requests')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # تحديث هذا السطر
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='under_review')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service.title} - {self.name}"
    
from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # الإشارة إلى موديل المستخدم
        on_delete=models.CASCADE,
        related_name="notifications"
    )
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.message[:20]}"