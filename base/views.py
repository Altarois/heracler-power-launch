from django.contrib import messages
from django.contrib.auth import authenticate, login as login_on
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User
from .forms import RegisterForm
from coach.models import salle
from django.contrib.auth import authenticate, login as login, logout
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user


# Create your views here.
def index(request):

    template = loader.get_template('base/index.html')
    return HttpResponse(template.render(request=request))

def salles(request):

    salles = salle.objects.all()
    print(salles)

    return render(request,'base/salle.html', context={"salles":salles})



@unauthenticated_user
def login_user(request):


    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = User.objects.get(email=email).username
        print(email)
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print("login successfuly")
            login(request, user)
            return HttpResponseRedirect('coach/dashboard')

        else:
            messages.info(request, 'Email or Password is incorrect')

    context={}
    return render(request, 'base/login.html', context)

def logout_user (request):
    logout(request)
    return HttpResponseRedirect('login')

@unauthenticated_user
def SignUp(request):
    #template= loader.get_template('base/signup.html')

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password1')
            type = form.cleaned_data.get('groups')
            print(type)
            group = Group.objects.get(id= type)
            #group = Group.objects.get(name="client")
            #user = authenticate(username=username, password=password)
            user = form.save()
            user.groups.add(group)
            messages.success(request, f'Account created successfully for {username}')
            return redirect('login')





    return render(request, 'base/signup.html', {'form': form})
