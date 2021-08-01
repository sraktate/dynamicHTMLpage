from django.shortcuts import render, redirect

from .forms import EventModelform
from .models import EventDetails
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def addevent(request):
    form = EventModelform()
    if request.method == 'POST':
        form = EventModelform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showevents')
    template_name = 'firstapp/addevent.html'
    context = {'form': form}
    return render(request, template_name, context)




def showevent(request):
    template_name = 'firstapp/showevents.html'
    events = EventDetails.objects.all()
    context = {'events':events}
    return render(request, template_name,context)

def homeview(request):
    template_name = 'firstapp/base.html'
    context = {}
    return render(request, template_name, context)
