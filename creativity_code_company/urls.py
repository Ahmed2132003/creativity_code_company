# company_website/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('services/', include('services.urls')),
    path('contact/', include('contact_us.urls')),
]

# إضافة ملفات الوسائط أثناء التطوير
if settings.DEBUG:  # تأكد من أن هذا الجزء يعمل فقط أثناء التطوير
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
