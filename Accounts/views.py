from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

def log_in(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        print(name)
        pass1 = request.POST.get('pass')
        print(pass1)
        if name:
            user = authenticate(username=name, password=pass1)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('Home')

        else:
            messages.error(request, "Input Username And PassWord")
    return render(request, 'login.html')


def reg(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        name = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 == pass2:
            if User.objects.filter(username=name).exists():
                messages.error(request, "Already Name is taken.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Already email is taken.")
            else:
                user = User.objects.create(username=name, first_name=f_name, last_name=l_name, email=email,
                                           password=pass1)
                user.set_password(pass1)
                user.save()
                messages.success(request, "User Registration Done.")
                return redirect('login')
        else:
            messages.error(request, "Password Not matched.")
    return render(request, 'registration.html')


def log_out(request):
    logout(request)
    return redirect('login')
