from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .models import Books
from django.contrib.auth.decorators import login_required

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
    books=Books.objects.all()
    

    return render(request, 'main.html',{'books':books})

@csrf_exempt
def cart(request):
    cart=request.session.get('cart',{}) #cart ka session uthaya
    cart_items=[] #list/array mein cart items store kiya
    for book_id,quantity in cart.items():
        book=Books.objects.get(id=book_id)
        cart_items.append({'book':book,'quantity':quantity})
    



    return render(request,'cart.html',{'cart_items':cart_items})

@csrf_exempt
def add_to_cart(request):
    cart=request.session['cart']
    





@csrf_exempt
@login_required
def profile(request):
    #print('hello')
    if(request.method=='POST'):
        print(request.POST)
    

    
    
    

    
    #return render(request,'profile.html',{'user':request.user, 'profile':request.user.profile})
    return render(request,'profile.html',{'user':request.user})

@csrf_exempt
#   @login_required
def logout_page(request):
    
    return render(request, 'logout.html')

def confirm_logout(request):
    logout(request)
    print('logged out mwah <3')
    return render(request, 'login.html')





# Create your views here.
