from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.template import loader
from .forms import ClientForm, CodeForm
from .models import client, stats
from coach.models import session, coach , task, exercise
from base.decorators import only_client
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied


# Create your views here.

@only_client
@login_required(login_url="login")
def clients(request):

    form = ClientForm
    context = {'form': form}
    return render(request, 'client/client.html', context= context)


@only_client
@login_required(login_url="login")
def home(request):

    form = CodeForm


    active= hasattr(request.user, 'client')
    print(active)

    if active:
        Cclient = client.objects.get(reference=request.user)
        client_session = session.objects.filter(clients=Cclient)

        context = {
            'active': active,
            'form': form,
            'session': client_session,
            'client':Cclient
        }

    else:

        context = {
            'active' : active,
            'form' : form,

        }

    if request.method == "POST":


        code = request.POST["code"]


        print(client)

        try:
            print("what else")
            real_client = client.objects.get(token=code)
            print(real_client)
            real_client.reference = request.user
            real_client.email = request.user.email
            real_client.name = request.user.username
            real_client.is_active = True
            real_client.save()
            messages.error(request, 'Code Correct !! (Votre compte a été activé.)')
            #real_client.update(reference = request.user , email = request.user.email, name = request.user.username , is_active = True)
            return HttpResponseRedirect('/client')


        except client.DoesNotExist:
            token = None
            print("client inexistant")
            messages.error(request, 'Wrong Code !! (Please Enter a correct Code)')



    return render(request, 'client/checkClient.html', context= context)


@only_client
@login_required(login_url="login")
def clients_session(request, session_id):


    try:
        current_session = session.objects.get(id=session_id)
    except session.DoesNotExist:
        raise Http404("This session dont exist.")

    Cclient = client.objects.get(reference=request.user)
    user_session = session.objects.filter(clients=Cclient)

    if current_session in user_session :
        tasks = task.objects.filter(session=session_id)
        context = {'tasks' : tasks, 'session' : current_session}

    else:
        raise PermissionDenied

    return render(request, 'client/Csession.html', context= context)

@login_required
def comment_submit(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        id = request.POST.get('session')
        print(id, comment_text)
        sess = session.objects.get(id=id)
        

        # Get the current user and session
        user = request.user

        # Create the comment
        comment = stats.objects.create(link=user,session_confirmed=sess, comment=comment_text)
        comment.save()

        # Pass the session object to the template
        context = {
            'session': session
        }

        # Redirect the user to a relevant page
        return HttpResponseRedirect('/sessions/',sess.id, context)  # Replace '/dashboard' with your desired URL


