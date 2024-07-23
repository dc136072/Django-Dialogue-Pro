from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'chatapp/index.html', context)

def signIn(request):
    context = {}
    return render(request, 'chatapp/signIn.html', context)

def signUp(request):
    context = {}
    return render(request, 'chatapp/signUp.html', context)