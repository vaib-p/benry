# service_requests/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('request/<int:pk>/status/', views.request_status, name='request_status'),
]
