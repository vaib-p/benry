# service_requests/views.py

from django.shortcuts import render, redirect
from .forms import ServiceRequestForm

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_status', pk=service_request.pk)
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})
