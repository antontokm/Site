from django.shortcuts import render, redirect
from .models import Driver, Forum
from .forms import ForumForm
from .api_request import add_drivers

def index(request):
    if request.POST.get('tableUpdate2021'):
        year = "2021"
        add_drivers(year)
    if request.POST.get('tableUpdate2022'):
        year = "2022"
        add_drivers(year)
    if request.POST.get('table2022'):
        drivers = Driver.objects.filter(year = '2022').order_by('-score')
        context = {'drivers': drivers}
        return render(request, 'Site_app/index.html', context)
    if request.POST.get('table2021'):
        drivers = Driver.objects.filter(year = '2021').order_by('-score')
        context = {'drivers': drivers}
        return render(request, 'Site_app/index.html', context)
    drivers = Driver.objects.filter(year = '2022').order_by('-score')
    context = {'drivers': drivers}
    return render(request, 'Site_app/index.html', context)

def forum(request):
    forums = Forum.objects.order_by('date_added')
    if request.method != 'POST':
        form = ForumForm()
    else:
        form = ForumForm(data=request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user_name = request.user
            f.save()
            return redirect('Site_app:forum')
    context = {'form': form, 'forums': forums}
    return render(request, 'Site_app/forum.html', context)
