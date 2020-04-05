from django.shortcuts import render,render,redirect
from django.http import HttpResponse
from django.contrib  import auth
from django.contrib.auth.models import User
from django.contrib  import auth
from django.contrib.auth.decorators import login_required
from taskmanager.models import Task
# Create your views here.


def index(request):
    tasks = Task.objects.all()
    return render(request,'index.html',{'tasks':tasks})

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        if user:
            auth.login(request,user)
            return redirect(dashboard)
        else:
            return render(request,'login.html',{'message':'Wrong Credentials'})
               
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email,is_staff=False).first()
        if user:
             return render(request,'register.html',{'message':'This username is already taken'})
        else:
            User.objects.create_user(email=email,username=username,password=password)
            return render(request,'register.html',{'message':'User Created succesfully'})   
    return render(request,'register.html')


@login_required(login_url='/login')
def dashboard(request):
    user = request.user
    tasks = Task.objects.filter(user=user).all()
    return render(request,'dashboard.html',{'tasks':tasks})

def delete(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    print(task)
    return redirect(dashboard)

def create(request):
    if request.method == "POST":
        user = request.user
        task_name = request.POST.get('name')
        task_description = request.POST.get('desc')
        start_date = request.POST.get('start')
        end_date = request.POST.get('end')
        task = Task(user=user,task_name=task_name, task_description=task_description,start_date=start_date,end_date=end_date)
        task.save()
        return render(request,'create.html',{'message':'Task Created'})
        
    return render(request,'create.html')

def invite(request,id):
    task = Task.objects.get(id=id)
    users = User.objects.filter(is_staff = False).all()
    return render(request,'invite.html',{'users':users,'task':task})



def edit(request,id):
    task = Task.objects.get(id=id)
    return render(request,'edit.html',{'task':task})

def logout(request):
    auth.logout(request)
    return redirect(index)