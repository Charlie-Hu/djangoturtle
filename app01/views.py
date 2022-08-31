from django.shortcuts import render, HttpResponse, redirect
from app01.models import Userinfo, Userplan
# Create your views here.


def index(request):
    return render(request, "index.html")


def login(request):
    customer = Userinfo.objects.all()
    print(customer)
    if request.method == 'GET':
        return render(request, "login.html")
    # print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    e = Userinfo.objects.filter(name=username).first()
    if e and password == e.password:
        return render(request, "main.html")
    return render(request, 'login.html', {"error_info": "invalid username or password"})


def register(request):
    if request.method == 'GET':
        return render(request, "register.html")
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")

    Userinfo.objects.create(name=user, password=pwd)
    return render(request, "jump.html")


def jump(request):
    return render(request, "jump.html")


def main(request):

    return render(request, "main.html")


def plan(request):
    if request.method == 'GET':
        return render(request, "plan.html")

    med_name = request.POST.get("med_name")
    dosage = request.POST.get("dosage")
    times = request.POST.get("times")
    num_time = request.POST.get("num_time")
    em_email = request.POST.get("email")

    Userplan.objects.create(medicine_name=med_name, dosage=dosage, times=times, num_time=num_time, email=em_email)
    return render(request, "main.html")

