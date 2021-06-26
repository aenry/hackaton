<<<<<<< HEAD
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
=======
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from .models import *
>>>>>>> 1f6a448014910d009fc2ac1861f43312e2bac318

# Create your views here.
def home(request):
    return render(request,'peoplemarket/home.html')


def empresadata(request):
<<<<<<< HEAD
    if request.method == 'POST':
        return redirect('/agregarproducto')
    return render(request, 'peoplemarket/empresadata.html')
=======
    tienda = frmTienda(request.POST or None)
    contexto = {
        'formulario' : frmTienda
    }
    if request.method=="POST":
        tienda.save()
        tienda.clean()
        return redirect(to='agregarproducto')
    return render(request, 'peoplemarket/empresadata.html',contexto)
>>>>>>> 1f6a448014910d009fc2ac1861f43312e2bac318

def agregarproducto(request):
    return render(request, 'peoplemarket/agregarproducto.html')

def seleccionarcampana(request):
    return render(request, 'peoplemarket/seleccionarcampana.html')
def registrocliente(request):
    return render(request, 'peoplemarket/registrocliente.html')
