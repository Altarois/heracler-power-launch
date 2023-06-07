from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:
            return HttpResponseRedirect('coach/dashboard')

        else:
             return view_func(request, *args, **kwargs)

    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            print('working', allowed_roles)

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles :
                print("you are a coach great")
                return view_func(request, *args, **kwargs)

            else:
                #return redirect(reverse('client'))
                print("you are a client great")
                return HttpResponse('you are not allowed to view this page')
                #return view_func(request, *args, **kwargs)

        return wrapper_func
    return decorator

def only_coach(view_func):
    def wrapper_function(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

            if group == 'client':
                print('redirecting clients')
                return HttpResponseRedirect('/client')


            if group == 'coach':
                return view_func(request, *args, **kwargs)

            else:
                return HttpResponseRedirect('/')

    return wrapper_function


def only_client(view_func):
    def wrapper_function(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

            if group == 'coach':
                print('redirecting clients')
                return HttpResponseRedirect('/coach/dashboard')


            if group == 'client':
                return view_func(request, *args, **kwargs)

            else:
                return HttpResponseRedirect('client')

    return wrapper_function