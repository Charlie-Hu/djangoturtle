from django.http import response, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from app01.models import Userplan
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


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
        return render(request, 'main.html')
    return render(request, 'login.html', {"error_info": "invalid username or password"})


def log_out(request):
    logout(request)
    return render(request, 'login.html')


def register(request):
    if request.method == 'GET':
        return render(request, "register.html")
    password = request.POST.get('pwd')
    print('password:'+password+'.')
    email = request.POST.get('email')
    username = request.POST.get('user')
    if password is None or email is None:
        return render(request, "register.html", {'state1': 'password or email cant be empty'})
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
    user_plan = Userplan.objects.filter(name=request.user.username).values()
    print(user_plan)
    return render(request, "main.html", {"user_plan": user_plan})


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
        print(per_num_time)
        num_time.append(per_num_time)
    print(num_time)
    em_email = request.POST.get("email")
    Userplan.objects.create(name=username, medicine_name=med_name, dosage=dosage, times=times, num_time=num_time,
                            email=em_email)
    return redirect("/main/")
