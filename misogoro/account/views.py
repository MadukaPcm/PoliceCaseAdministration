from django.shortcuts import render, redirect
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def HomepageView(request):
    
    context ={}
    return render(request, 'homepage.html', context)

def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        user = authenticate(username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)

            return redirect('dashboardpolice_url')

        else:
            messages.info(request, 'invalid username || password')
            return redirect('login_url')

    context = {}
    return render(request, 'account/login.html', context)

def RegisterView(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        first_name = request.POST.get('First_name')
        last_name = request.POST.get('Last_name')
        email = request.POST.get('Email')
        password1 = request.POST.get('Password1')
        password2 = request.POST.get('Password2')

        if User.objects.filter(username=request.POST['Username']).exists():
            messages.info(request, 'username already exist')
            return redirect('register_url')

        elif password1 != password2:
            messages.info(request, 'password does not match')
            return redirect('register_url')
        else:
            userdata = User.objects.create_user(username=username,email=email,password=password1)
            userdata.first_name = first_name
            userdata.last_name = last_name
            userdata.save()

            return redirect('login_url')
    
    context = {}
    return render(request, 'account/register.html', context)

def LogoutView(request):
    logout(request)
    return redirect('homepage_url')

def ForgotPasswordView(request):
    
    context = {}
    return render(request, 'account/forgotpassword.html', context)
    