from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_view, logout
from .forms import UserForm


# Create your views here.
def index(request):
    context = {}
    return render(request, 'chatapp/index.html', context)

def login(request):
    context = {}
    return render(request, 'chatapp/login.html', context)

def signUp(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login_view(request, user)
                return redirect('index')
    context = {'form': form}
    return render(request, 'chatapp/signUp.html', context)