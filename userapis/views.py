from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout


@csrf_exempt
def login_data(request):
    error_message=None
    if request.method=="POST":
        #login_data=request.POST
        #print(login_data)
        
        username = request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            
            login(request, user)
            return redirect("/main")
        else:
            error_message="username or password is not valid"
           


        
    return render(request, 'login.html', {"error_message":error_message})



@csrf_exempt
def register(request):
    if request.method=='POST':
        userinfo=request.POST
        #print(userinfo)
        user=User.objects.create_user(username=userinfo["username"],password=userinfo["password"],email=userinfo["email"])
        user.save()
    return render(request, 'register.html')

@csrf_exempt
def main(request):
    return render(request, 'main.html')
# Create your views here.
