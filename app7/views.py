from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import HospitalizacionForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def holamundo(request):
    return HttpResponse("Helloo")

def home(request):
    return render(request, "home.html")
def registro(request):
    if request.method == 'GET':
        return render(request, "registro.html",{
        "form":UserCreationForm
        })
    else: 
        req = request.POST
        if req['password1']==req['password2']:
            try:
                user = User.objects.create_user(
                    username=req['username'],
                    password=req['password1']
                )
                user.save()
                login(request, user)
                return redirect('/')
            except IntegrityError as ie:
                return render(request, "registro.html",{
                "form":UserCreationForm,
                "msg":"Eres un impostor, ese usuario ya existe."
        })
            except Exception as e:
                return render(request, "registro.html",{
                        "form":UserCreationForm,
                        "msg":f"Se ha presentado el siguiente error {e}"
                })
            
        else:
            return render(request, "registro.html",{
                "form":UserCreationForm,
                "msg":"Favor de verificar que la contraseña coincida."
        })
            
def iniciarSesion(request):
    if request.method == "GET":
        return render(request,"login.html", {
            "form":AuthenticationForm,
        })
    else:
        try:
            user=authenticate(request,
                            username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                login(request,user)
                return redirect("/")
            else:
                return render(request,"login.html", {
                "form":AuthenticationForm,
                "msg":"Te atrapé. El usuario o contraseña son incorrectos, impostor."
                })
        except Exception as e:
            return render(request,"login.html", {
                "form":AuthenticationForm,
                "msg":f"Hubo un error{e}"
            })
        
def cerrarsesion(request):
    logout(request)
    return redirect("/")

@login_required
def nuevaHospitalizacion(request):
    if request.method == "GET":
        return render(request,"nuevahosp.html", {
                    "form":HospitalizacionForm
                })
    else:
        try:
            form = HospitalizacionForm(request.POST)
            if form.is_valid():
                nuevo=form.save(commit=False)
                if request.user.is_authenticated:
                    nuevo.usuario = request.user
                    nuevo.save()
                    return redirect("/")
                else:
                    return render(request,"nuevahosp.html", {
                        "form":HospitalizacionForm,
                        "msg":"Disculpe, usted debe autenticarse."
                    })
            else:
                return render(request,"nuevahosp.html", {
                        "form":HospitalizacionForm,
                        "msg":"Este formulario no es válido."
                    })
        except Exception as e:
            return render(request,"nuevahosp.html",{
                "form":HospitalizacionForm,
                "msg":f"Hubo un error {e}"
            })
            