# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
]

urlpatterns += [
    path('logout/', LogoutView.as_view(), name='logout'),
]
