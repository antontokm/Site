from django.shortcuts import render

def index(request):
    return render(request, 'Site_app/index.html')
