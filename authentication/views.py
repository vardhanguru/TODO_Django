from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def auth(request):
    return render(request,'authentication/index.html')


def signup(request):

    if request.method=='POST':
        username=request.POST['Username']
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['psw']
        password2=request.POST['psw2']
        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=firstname
        myuser.last_name=lastname
        myuser.save()
        messages.success(request,"your account has been successfully created!")

        return redirect("/signin")
    return render(request,'authentication/signup.html')

def signin(request):

    if request.method=="POST":
        username=request.POST['username']
        psw=request.POST['psw']
        user=authenticate(username=username,password=psw)
        print('jer')
        print(user)
        print("hi")
        if user is not None:
            print('jer')
            print(user.first_name)
            login(request,user)
            fname=user.first_name
            request.session['logged_in_username'] = user.username
            return redirect('all-tasks')
        else:
            messages.error(request,"bad credentials")
            return redirect("/signin")
    return render(request,'authentication/signin.html')

from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signout(request):
    logout(request)
    return redirect('todo-home')



