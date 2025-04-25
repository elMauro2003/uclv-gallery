from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from apps.accounts.decorators import user_is_not_authenticated
from django.contrib.auth.decorators import login_required 

# Create your views here.

def index(request):
    return render(request, 'index.html')


@user_is_not_authenticated
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next_url =  request.POST.get('next','')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            context = {
                "error":"Credenciales incorrectas!",
            }
            return render(request, 'pages/accounts/login.html',context)
    context = {
        "next":request.GET.get('next', ''),
    }
    return render(request, 'pages/accounts/login.html',context)