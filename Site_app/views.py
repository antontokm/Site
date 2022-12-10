from django.shortcuts import render, redirect
from .models import Driver, Forum
from .forms import ForumForm
from .api_request import add_drivers

def index(request):
    if request.POST.get('updateTable'):
        add_drivers()   
    drivers = Driver.objects.order_by('-score')
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
