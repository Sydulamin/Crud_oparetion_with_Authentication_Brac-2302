import os

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.


def Home(request):
    return render(request, 'base.html')

@login_required(login_url='login')
def Create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        birth_day = request.POST['birth_day']
        address = request.POST['address']
        img = request.FILES.get('img')
        if img:
            if name:
                a = Profile(name=name, image=img, address=address, email=email, Birth_day=birth_day,
                            Gender=gender, phone_number=phone, age=age)
                a.save()
                return redirect('allProf')
            else:
                messages.success(request, 'Please Fill Up All Fields.')
                return redirect('Create')
        else:
            a = Profile.objects.create(name=name, address=address, email=email, Birth_day=birth_day,
                                       Gender=gender, phone_number=phone, age=age)
            a.save()
            return redirect('allProf')

    return render(request, 'Create.html')


@login_required(login_url='login')
def allProf(request):
    serach = request.GET.get('search')
    if serach:
        all_prof = Profile.objects.filter(Q(name__icontains=serach) | Q(email__icontains=serach))
    else:
        all_prof = Profile.objects.all()
    context = {
        'all': all_prof,
    }
    return render(request, 'AllProf.html', context)


@login_required(login_url='login')
def singleProf(request, id):
    i = Profile.objects.get(id=id)
    return render(request, 'SIngleProf.html', locals())


@login_required(login_url='login')
def deleteProf(request, id):
    prof = Profile.objects.get(id=id)
    if prof.image != 'defult/defult.jpg':
        os.remove(prof.image.path)
    prof.delete()
    return redirect('allProf')


@login_required(login_url='login')
def updateProfile(request, id):
    prof = Profile.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        birth_day = request.POST['birth_day']
        address = request.POST['address']
        img = request.FILES.get('img')
        if img:
            if prof.image != 'defult/defult.jpg':
                os.remove(prof.image.path)

            prof.image = img
            prof.name = name
            prof.email = email
            prof.age = age
            prof.gender = gender
            prof.phone = phone
            prof.birth_day = birth_day
            prof.address = address
            prof.save()
            messages.success(request, 'Update Done.')
            return redirect ('allProf')
        else:
            prof.name = name
            prof.email = email
            prof.age = age
            prof.gender = gender
            prof.phone = phone
            prof.birth_day = birth_day
            prof.address = address
            prof.save()
            messages.success(request, 'Update Done.')
            return redirect('allProf')
    return render(request, 'updateProf.html', locals())
