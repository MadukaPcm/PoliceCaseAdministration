from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

# A decorator for allowing admins(user) to access the page..
def un_co(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser == 1:
                return redirect('/admin')
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                if group == 'co':
                    return view_func(request, *args, **kwargs)
                if group == 'police':
                    return redirect('dashboardpolice_url')
                if group == 'explorer':
                    return redirect('dashboardexplorer_url')
            else:
                messages.info(request, 'Ur None A member')
                return redirect('login_url')
        else:
            return request('login_url')

    return wrapper_func

# A decorator for allowing an expert(user) to access the page..
def un_police(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser == 1:
                return redirect('/admin')
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                if group == 'police':
                    return view_func(request, *args, **kwargs)
                if group == 'co':
                    return redirect('dashboardco_url')
                if group == 'explorer':
                    return redirect('dashboardexplorer_url')
            else:
                messages.info(request, 'Ur None A member')
                return redirect('login_url')
        else:
            return request('login_url')

    return wrapper_func

def un_explorer(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser == 1:
                return redirect('/admin')
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                if group == 'explorer':
                    return view_func(request, *args, **kwargs)
                if group == 'co':
                    return redirect('dashboardco_url')
                if group == 'police':
                    return redirect('dashboardpolice_url')
            else:
                messages.info(request, 'Ur None A member')
                return redirect('login_url')

        else:
            return request('login_url')

    return wrapper_func