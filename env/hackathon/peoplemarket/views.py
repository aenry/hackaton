from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'peoplemarket/home.html')
def empresadata(request):
    return render(request, 'peoplemarket/empresadata.html')

def agregarproducto(request):
    return render(request, 'peoplemarket/agregarproducto.html')

