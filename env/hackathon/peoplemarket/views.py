from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    return render(request,'peoplemarket/home.html')
def empresadata(request):
    if request.method == 'POST':
        return redirect('/agregarproducto')
    return render(request, 'peoplemarket/empresadata.html')

def agregarproducto(request):
    return render(request, 'peoplemarket/agregarproducto.html')

def seleccionarcampana(request):
    return render(request, 'peoplemarket/seleccionarcampana.html')
def registrocliente(request):
    return render(request, 'peoplemarket/registrocliente.html')
