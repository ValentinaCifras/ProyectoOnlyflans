from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Flan, ContactForm, PromocionTortas
from .forms import ContactFormForm, ContactFormModelForm

# Create your views here.
def indice(request):
    flanes = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes})

def acerca(request):
    return render(request,'about.html', {})

@login_required
def bienvenido(request):
    flanes = Flan.objects.filter(is_private=True)
    promociones_tortas = PromocionTortas.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes, 'promociones_tortas': promociones_tortas})

def contacto(request):
    if request.method =='POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)

            return HttpResponseRedirect('/exito')
    
    else:
        form = ContactFormForm()

    return render(request,'contacto.html', {'form':form})


def exito(request):
    return render(request,'exito.html', {})

def ubicacion(request):
    return render(request,'ubicacion.html', {})

