from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def loginview(request):
    if request.method == 'POST':
        u = request.POST.get('un')
        p = request.POST.get('Pass')
        user = authenticate(username=u, password=p)

        if user is not None:
            login(request, user)
            return redirect('addevent')
        else:
            messages.error(request, 'Invalid Credentials')

    template_name = 'secondapp/login.html'
    context = {}
    return render(request, template_name, context)


def registerview(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'secondapp/register.html'
    context = {'form': form}
    return render(request, template_name, context)


def logoutview(request):
    logout(request)
    return redirect('login')
