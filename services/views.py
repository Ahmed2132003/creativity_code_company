from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Service, ServiceRequest
from .forms import ServiceRequestForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Notification, ServiceRequest
@login_required
def service_request_view(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.service = service
            service_request.user = request.user
            service_request.save()

            # إرسال الإشعار بالبريد الإلكتروني
            # إنشاء إشعار
            Notification.objects.create(
                user=request.user,
                message=f" your request for the service{service.title} has been received we will contact you soon"
            )

            return redirect('service_request_success')
    else:
        form = ServiceRequestForm()

    return render(request, 'services/service_request_form.html', {'form': form, 'service': service})
from django.shortcuts import render
from .models import Service

def service_list_view(request):
    services = Service.objects.all()  # استرجاع جميع الخدمات
    return render(request, 'services/service_list.html', {'services': services})
def service_request_success_view(request):
    return render(request, 'services/service_request_success.html')
@login_required
def user_service_requests_view(request):
    user_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'services/user_requests.html', {'user_requests': user_requests})

def notifications_view(request):
    # الحصول على جميع الإشعارات الخاصة بالمستخدم
    notifications = Notification.objects.filter(user=request.user).order_by("-created_at")

    # تحديث الإشعارات غير المقروءة
    notifications.update(is_read=True)

    # حساب عدد الإشعارات غير المقروءة
    notifications_count = Notification.objects.filter(user=request.user, is_read=False).count()

    # عرض الصفحة مع الإشعارات
    return render(request, "services/notifications.html", {
        "notifications": notifications,
        "notifications_count": notifications_count,
    })

@login_required
def mark_notification_read(request, notification_id):
    # تحديد الإشعار
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect("notifications")