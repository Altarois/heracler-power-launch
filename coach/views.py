from tempfile import template
from django.core.serializers import serialize
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import coach, client, session, exercise, task, category
from django.template import loader
from django.views.generic import View
from django.core import serializers
from django.core.exceptions import PermissionDenied

from django.contrib.auth.decorators import login_required
from base.decorators import allowed_users, only_coach

from django.http import JsonResponse
from django.forms.models import model_to_dict

from .forms import ExerciseForm, SessionForm, SessionUpdate

from client.forms import ClientForm


# render the index.html and return in HttpReponse()
def index(request):
    # coachs=coach.objects.all().values_list('name', flat=True)
    # message = """<ul>{}<ul>""".format("\n".join(coachs))


    template = loader.get_template('coach/index.html')
    return HttpResponseRedirect('/coach/dashboard')


def login(request):
    # coachs=coach.objects.all().values_list('name', flat=True)
    # message = """<ul>{}<ul>""".format("\n".join(coachs))
    template = loader.get_template('coach/login.html')
    return HttpResponse(template.render(request=request))



@login_required(login_url="login")
@only_coach
def dashboard(request):
    clients = client.objects.filter(affiliation=request.user)
    sessions = session.objects.filter(clients__in=clients)

    for cli in clients:
        print("Client:", cli.name)
        for sess in cli.sessions.all():
            print("Session:", sess.name)


    return render(request, 'coach/dashboard.html', context={'clients': clients, 'sessions': sessions})


@only_coach
@login_required(login_url="login")
def coach_session(request):

    sessions = session.objects.filter(coach= request.user.id)
    form = SessionForm()

    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            detail = request.POST.get('detail')
            coach_id = request.user.id
            obj= session.objects.create(name=name,detail=detail,coach_id=coach_id)


            return redirect('addsession/'+str(obj.id) )






    return render(request, 'coach/session.html', context={'sessions': sessions, 'form': form})



@only_coach
@login_required(login_url="login")
def addsession(request, session_id):

        template = loader.get_template('coach/addexercise.html')


        user_session = session.objects.filter(coach=request.user)
        #check_session = get_object_or_404(session, coach=session_id)

        try:
            current_session = session.objects.get(id=session_id)
        except session.DoesNotExist:
            raise Http404("This session dont exist.")



        if current_session in user_session :
            exercises = exercise.objects.all()
            categories = category.objects.all()
            id = request.POST.get("id")
            # context = {'exercises': exercises}
            UpperBody = exercise.objects.filter(category__name="Upper Body")
            LowerBody = exercise.objects.filter(category__name="Lower Body")
            FIIT = exercise.objects.filter(category__name="FIIT")
            LIIT = exercise.objects.filter(category__name="LIIT")
            form = ExerciseForm()
            tasks = task.objects.filter(session=session_id)
            print(id)

            AllinOne = [str([UpperBody]),str([LIIT]),str([FIIT]),str([LowerBody])]

            ziped_data = zip(categories,AllinOne)


            context = {'exercises': exercises,
                            'categories': categories,
                           'UpperBody': UpperBody,
                           'LowerBody': LowerBody,
                           'FIIT': FIIT,
                           'LIIT': LIIT,
                           'form': form,
                           'tasks': tasks,
                            'AllinOne': AllinOne,
                            'ziped_data': ziped_data,
                            'session': current_session
                           }

            form = ExerciseForm()





            if request.method == 'POST' and request.POST['action'] == 'tasks':
                    #form = ExerciseForm(request.POST)

                    name = request.POST.get("exename")
                    id = request.POST.get("id")
                    des = request.POST.get("description")
                    set = request.POST.get("set")
                    rest = request.POST.get("rest_time")
                    print(set)
                    print(des)
                    current_exe = exercise.objects.get(id=id)
                    new_task = task.objects.create(name=name, description= des, set=set, rest_time=rest , reference = current_exe ,session=current_session)
                    print('adding task', new_task)
                    print(new_task)

                    return JsonResponse({'task': model_to_dict(new_task)}, status=200)




            if request.method == 'POST' and request.POST['action'] == 'search':
                #form = ExerciseForm(request.POST)
                print(form)
                new_task = request.POST.get("name")
                print('adding task', new_task)
                new_exrercise = task.objects.create(name=new_task, session=current_session)
                return JsonResponse({'task': model_to_dict(new_exrercise)}, status=200 )

            if request.method == 'POST' and request.POST['action'] == None:
                print("identifiant de session envoyer")


        else:
            raise PermissionDenied






        return render(request, 'coach/addexercise.html', context=context)








class sessionComplete(View):
    def post(self, request, id):
        tache= task.objects.get(id=id)
        tache.completed= True
        print(tache.completed)
        tache.save()
        return JsonResponse({'task': model_to_dict(tache)}, status=200)



class delete(View):
    def post(self, request , id):
        tache = task.objects.get(id=id)
        tache.delete()
        return JsonResponse({'result': 'ok'}, status=200)

class exo(View):
    def get(self, request):


        form = ExerciseForm()
        tasks = task.objects.all()

        return render(request, 'coach/test.html', {'form': form, 'tasks': tasks })

    def post(self, request):

        form = ExerciseForm(request.POST)

        if form.is_valid():
            print('adding task', form)
            new_exrercise = form.save()
            return JsonResponse({'task': model_to_dict(new_exrercise)}, status=200 )
        else:
            print('not adding task')
            return redirect('exo')


class add_exo(View):


    def post(self, request):

        print("hey hey 2")
        if request.is_ajax() and request.method == 'POST':
            print('adding task to the form')
            exe = request.POST['add']
            new_exrercise = task.objects.create(name=exe)
            return JsonResponse({'task': model_to_dict(new_exrercise)}, status=200 )
        else:
            print('not adding task')
            return redirect('addsession')



@login_required(login_url="login")
@only_coach
def testview(request):
    template = loader.get_template('coach/addexercise.html')
    form = ExerciseForm()
    tasks = task.objects.all()
    context = {
        'form': form,
        'tasks': tasks
    }
    return HttpResponse(template.render(context, request=request))

    form = ExerciseForm(request.POST)

    if form.is_valid():
        print('adding task')
        new_exrercise = form.save()
        return redirect('session')
    else:
        print('not adding task')
        return redirect('session')


@login_required(login_url="login")
@only_coach
def view_client(request, coach_id):
    clients = client.objects.filter(affiliation_id=coach_id)
    coachs = coach.objects.get(pk=coach_id)
    strC = len(clients)
    message = "client du coach " + str(coachs) + "<br>"
    for i in range(0, strC):
        message += "client numéro " + str(i + 1) + " est " + str(clients[i]) + "<br>"

    return HttpResponse(message)


@login_required(login_url="login")
@only_coach
def search(request):
    query = request.GET.get('query')
    if not query:
        message = "Aucun exercise trouvé"
    else:
        Qexercise = session.objects.filter(name__icontains=query)

        if not Qexercise.exists():
            Qexercise = session.objects.filter(coach__name__icontains=query)

        if not Qexercise.exists():
            message = "bien ou quoi t'habite dans le coin ou quoi"

        else:
            message = "résultat :" + str(Qexercise[0]) + "<br>"

    return HttpResponse(message)


@only_coach
@login_required(login_url="login")
def addclient(request):
    form = ClientForm()
    clients = client.objects.filter(affiliation=request.user.id)
    Csession = session.objects.filter(coach=request.user.id)

    context = {'form': form ,'clients': clients , 'Csession' : Csession}

    #form = ClientForm
    if request.method == 'POST' and request.POST['action'] == 'client':
        form = ClientForm(request.POST)
        print(form)
        name = request.POST.get('name')
        email = request.POST.get('email')

        #client_code = code.objects.create()

        new_client = client.objects.create(name = name, email = email, affiliation = request.user)
        new_client.save()
        return JsonResponse({'client': model_to_dict(new_client)}, status=200)

        '''if form.is_valid():
            print('adding client 1133 to the hell', form)
            name = request.POST.get('name')
            email = request.POST.get('email')
            new_client = client.objects.create(name= name, email=email , affiliation=request.user)
            new_client.save()
            return JsonResponse({'client': model_to_dict(new_client)}, status=200)

        else:
            print('not adding client to the form 1333 dahell')

            return redirect('addclient')'''


            #return JsonResponse({'session': model_to_dict(Sclient)}, status=200)
    else:
        print('not adding task')
        #return redirect('addclient')

    if request.method == 'POST' and request.POST['action'] == 'session':
        print("session response")
        id = request.POST.get('id')
        print(id)
        #Sclient = list(session.objects.filter(coach=request.user.id))
        Sclient = session.objects.filter(clients__id=id)

        SerializedQuery = serializers.serialize('json', Sclient)

        return JsonResponse(SerializedQuery, safe=False)

    if request.method == 'POST' and request.POST['action'] == 'active':
        print("active response")
        id = request.POST.get('id')
        client_id= request.POST.get('ClientID')
        print(id)
        current_session = session.objects.get(id=id)
        client_session = session.objects.filter(clients__id=client_id)
        current_client = client.objects.get(id=client_id)
        print(current_session)
        print(client_session)

        if  current_session not in client_session:
            print("adding the good session")
            current_session.clients.add(current_client)
            current_session.save()
            print(current_session)
            SerializedSession = serializers.serialize('json', current_session)

            #return JsonResponse(SerializedSession, safe=False)
            return JsonResponse({'session': model_to_dict(current_session)}, status=200)

        else:
            print("session deja existente pour ce client")
            #return JsonResponse({"success": False, "error": "there was an error"})

    if request.method == 'POST' and request.POST['action'] == 'show':
        print("show response")
        id = request.POST.get('id')

        shown_client =  client.objects.get(id=id)
        return JsonResponse({'code': model_to_dict(shown_client)}, status=200)

    return render(request, 'coach/addclient.html', context= context)


@only_coach
@login_required(login_url="login")
def pt_profile(request):
    template = loader.get_template('coach/pt-profile.html')
    return HttpResponse(template.render(request=request))

class affiliate(View):
    def get(self, request):


        form = ClientForm()
        clients = client.objects.filter(affiliation=request.user.id)

        return render(request, 'coach/addclient.html', {'form': form, 'clients': clients })

    def post(self, request):

        form = ClientForm(request.POST)

        if form.is_valid():
            print('adding client')

            name = request.POST.get('name')
            email = request.POST.get('email')
            code = code.objects.create(reference=request.user.id)
            new_client = client.objects.create(name=name, email=email, affiliation=request.user, token=code)
            new_client.save()
            return JsonResponse({'client': model_to_dict(new_client)}, status=200 )
        else:
            print('not adding client 123')
            return redirect('affiliation')


class show_session(View):

    def get(self, request , id):
        Sclient = session.objects.all()
        #Sclient = session.objects.filter(client__id=id)
        context = { 'Sclient': Sclient }

        #return redirect('addclient',context=context)

        return render(request, 'coach/addclient.html', { 'Sclient': Sclient })


def attribute_session(request , name):



    #form for session update



    form = SessionUpdate()
    #clients = client.objects.filter(affiliation=request.user)
    sessions = session.objects.filter(coach=request.user)




    try:
        user_client = client.objects.get(name=name)
        client_session = session.objects.filter(clients=user_client)
        client_Notsession = session.objects.exclude(clients=user_client)
    except client.DoesNotExist:
        raise Http404("This client dont exist.")


    check_client = client.objects.filter(affiliation= request.user)



    if request.method == "POST":


            # form = SessionUpdate(request.POST)
            nameru = request.POST.get("name", None)
            detail = request.POST.get("detail")
            estimation = request.POST.get("estimation", None)
            timing = request.POST.get("timing")
            id = request.POST.get("id")
            print("lmao")
            print(id)

            if nameru and int(estimation)>0 :

                '''times=datetime.datetime.strptime(timing, "%d/%m/%Y %H:%M:%S.%f").date()
                date_time = times.strptime(date_string, "%d/%m/%Y %H:%M:%S.%f")'''
                print(timing)

                print(name)

                print("yow le rap")
                current_session = session.objects.get(id=id)
                if current_session in sessions :

                    current_session.name = nameru
                    current_session.detail = detail
                    current_session.estimation = estimation
                    current_session.clients.add(user_client)
                    current_session.save()
                    messages.info(request, 'Client session updated succefuly')
                    return HttpResponseRedirect('/coach/manage/'+name+'#'+nameru)
                    #return JsonResponse({'session': model_to_dict(current_session)}, status=200)

                else:
                    raise PermissionDenied

            else:
                print("hey pas de rap")
                messages.error(request, 'please enter correct value or fill all fields')
            '''#client_session = session.objects.filter(clients__id=client_id)
            
            current_session.name = nameru
            current_session.detail = detail
            current_session.estimation = estimation
            # current_session.timing=timing
            current_session.clients.add(user_client)
            
            print(current_session)'''

        #return JsonResponse({'session': model_to_dict(current_session)}, status=200)







    context = {'sessions': sessions, 'form':form, 'client_session': client_session , 'Notsession': client_Notsession ,'client': user_client }


    return render(request, 'coach/ManageClient.html', context=context)

