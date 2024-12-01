# models.py in service_requests app
from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    TYPE_CHOICES = [
        ('installation', 'Installation'),
        ('repair', 'Repair'),
        ('maintenance', 'Maintenance'),
    ]
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    details = models.TextField()
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.request_type} request from {self.customer.username}"

class FileAttachment(models.Model):
    request = models.ForeignKey(ServiceRequest, related_name="attachments", on_delete=models.CASCADE)
    file = models.FileField(upload_to='service_requests/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
