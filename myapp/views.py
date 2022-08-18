from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as LogIn
from django.contrib.auth import logout as LogOut
from myapp.forms import TaskForm
from myapp.models import Tasks
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        tasklu=Tasks.objects.filter(owner=request.user)
    else:
        tasklu="no"
    return render(request,'myapp/index.html',{'tasks':tasklu})

def signin(request):
    if request.method=="POST":
        try:
            user = User.objects.create(
            username=request.POST.get("username"),
            password=request.POST.get("username"),
            email=request.POST.get("email"),
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name")
            )
            user.save()
        except:
            return HttpResponse("Username Already Taken Please Try Unique Name")
        if user:
            return render(request,'myapp/index.html')
        else:
            return render(request,'myapp/index.html',{'username':False})
    return render(request,'myapp/signin.html')

def login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            use=authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
            if use:
                LogIn(request,use)
                return index(request)
            else:
                return HttpResponse("Log in Failed")
    else:
        return render(request,'myapp/index.html')
    return render(request,'myapp/login.html')

def logout(request):
    LogOut(request)
    return login(request)

def add_task(request):
    if request.user.is_authenticated:
        form=TaskForm()
        if request.method=="POST":
            form=TaskForm(request.POST)
            if form.is_valid():
                Tasks.objects.create(owner=request.user,title=request.POST.get('title'),deadline=request.POST.get('deadline'))
                Tasks.save
                return index(request)
            else:
                form=TaskForm()
        else:
            return render(request,'myapp/create_task.html',{'form':form})

def delete_task(request,pk=None):
    if(request.method=="POST"):
        obj=get_object_or_404(Tasks,pk=pk)
        obj.delete()
        return index(request)
    else:
        return render(request,'myapp/delete_task.html')