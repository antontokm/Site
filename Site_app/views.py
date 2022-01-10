from django.shortcuts import render
from .models import Driver

def index(request):
    return render(request, 'Site_app/index.html')

def  drivers(request):
    drivers = Driver.objects.order_by('date_added')
    context = {'drivers': drivers}
    return render(request, 'learning_logs/index.html', context)

