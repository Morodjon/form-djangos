from django.shortcuts import render, redirect
from .forms import UserProfilForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserProfilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserProfilForm()
    return render(request, 'register.html', {'form':form})

def success(request):
    return render(request, 'success.html')

    