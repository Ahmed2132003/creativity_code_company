from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list_view, name='service_list'),  # إضافة هذا السطر
    path('service/<int:service_id>/request/', views.service_request_view, name='service_request'),
    path('service/request/success/', views.service_request_success_view, name='service_request_success'),
    path('user/requests/', views.user_service_requests_view, name='user_requests'),
    path("notifications/", views.notifications_view, name="notifications"),
    path("notifications/<int:notification_id>/mark-read/", views.mark_notification_read, name="mark_notification_read"),
]

