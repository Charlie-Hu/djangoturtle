from django.shortcuts import render, HttpResponse, redirect
from app01.models import Userinfo
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
    return HttpResponse('successful')
    return redirect('/login')


def main(request):
    return render(request, "main.html")

