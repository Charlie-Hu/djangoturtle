from django.http import response, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from rest_framework.response import Response

from app01.models import Userplan
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from app01.serializer import HardwareDataSerializer
from django.core.mail import send_mail
import time

# Create your views here.
from djangoturtle import settings


def index(request):
    return render(request, "index.html")


def log_in(request):
    if request.method == 'GET':
        return render(request, "login.html")
    username = request.POST["user"]
    password = request.POST["pwd"]
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/main/')
    return render(request, 'login.html', {"error_info": "invalid username or password"})


def log_out(request):
    logout(request)
    return render(request, 'login.html')


def register(request):
    if request.method == 'GET':
        return render(request, "register.html")
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    username = request.POST.get('user')
    # print(password)
    if len(password) < 1 or len(email) < 1 or len(username) < 1:
        return render(request, "register.html", {'state1': 'input detail can not be empty'})
    elif User.objects.filter(username=username):
        return render(request, "register.html", {'state2': 'user_exist'})
    else:
        new_user = User.objects.create_user(username=username, password=password, email=email)
        new_user.save()
        return render(request, "jump.html")


def jump(request):
    return render(request, "jump.html")


@login_required
def main(request):
    if request.method == 'GET':
        user_plan = Userplan.objects.filter(name=request.user.username).values()
        return render(request, "main.html", {"user_plan": user_plan})


@csrf_exempt
@login_required
def plan_delete(request):
    items_to_delete = request.GET.get('id')
    Userplan.objects.filter(id=items_to_delete).delete()
    print('1')
    return HttpResponse('delete successful')


@login_required
def plan(request):
    if request.method == 'GET':
        return render(request, "plan.html")
    username = request.user.username
    med_name = request.POST.get("med_name")
    dosage = request.POST.get("dosage")
    times = request.POST.get("times")
    num_time = list()
    for i in range(0, int(times)):
        per_num_time = request.POST.get('num_time{num}'.format(num=i))
        num_time.append(per_num_time)

    em_email = request.POST.get("email")
    if len(med_name) < 1 or len(dosage) < 1 or len(times) < 1 or len(num_time) < 1:
        return render(request, "plan.html", {"state1": "input detail can not be empty"})
    new_time = ',  '.join(num_time)
    Userplan.objects.create(name=username, medicine_name=med_name, dosage=dosage, times=times, num_time=new_time,
                            email=em_email)
    return redirect("/main/")


class Hardware_View(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Userplan.objects.all()
        username = request.GET.get('username')
        psw = request.GET.get('password')
        user = authenticate(username=username, password=psw)
        self_email = User.objects.filter(username=user).values("email").first()
        print(psw, username)
        ser = HardwareDataSerializer(instance=queryset, many=True)
        fl_data = dict()
        if user is not None:
            for item in ser.data:
                if username == item.get("name"):
                    if item.get("name") not in fl_data:
                        fl_data[item.get("name")] = list()
                        fl_data["self_email"] = self_email["email"]
                    fl_data[item.get("name")].append(item)

            return Response(fl_data)
        return HttpResponse('invalid username or password')


@csrf_exempt
def send_email(request):
    medicine_status = request.GET.get("medicine_status")
    print(type(medicine_status))
    em_email = request.GET.get("b_email")
    self_email = request.GET.get("s_email")
    if medicine_status == '1':
        send_mail(
            'Emergency',
            'Please check senior status.',
            settings.EMAIL_HOST_USER,
            [em_email],
            fail_silently=False,
        )
        return HttpResponse('send email')
    elif medicine_status == '0':
        send_mail(
            'Notice',
            'Please take your medication on time.',
            settings.EMAIL_HOST_USER,
            [self_email],
            fail_silently=False,
        )
        return HttpResponse('send email')
    return HttpResponse('unknown status.')
