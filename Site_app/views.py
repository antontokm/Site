from django.shortcuts import render
from .models import Driver

def index(request):
    drivers = Driver.objects.order_by('-score')
    context = {'drivers': drivers}
    return render(request, 'Site_app/index.html', context)

