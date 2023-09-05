from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth import update_session_auth_hash
from . models import *
from django.db.models import Sum
from django.contrib.auth.models import auth
from django.contrib import messages
# Create your views here.

def index(request):
    movies = MovieDetails.objects.all()
    
    context = {
        'mov': movies
    }
    return render(request,"index.html", context)

def login(request):
    if request.method=='POST':
        mid = request.POST['mailid']
        password = request.POST['password']
        
        if User_Info.objects.filter(email = mid, password = password).exists():
            user = User_Info.objects.get(email=mid)
            return redirect('/')
        else:
            messages.error(request,'Username/Password is incorrect')
            return redirect('login')
    else:
        return render(request,"login.html")


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User_Info.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
            elif User_Info.objects.filter(email=email).exists():
                messages.info(request,'email already exist')
            else:        
                user = User_Info.objects.create_user(username = username, first_name= first_name, last_name= last_name, email=email,password=password1)
                user.save()
                messages.info(request,'User created')
                return redirect('login')
        else:
            messages.info(request, 'Password not match')
        return redirect('register')                 
    else:
        return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def movies(request, id):
    #cin = Cinema.objects.filter(shows__movie=id).distinct()
    movies = MovieDetails.objects.get(movie=id)
    context = {
        'movies':movies,
        
    }
    return render(request, "movies.html", context )