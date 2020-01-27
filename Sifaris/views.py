from django.shortcuts import render,redirect
from .models import Pizza,Olcu
from .forms import Sifaris_Form,Elave_sifaris
from django.forms import formset_factory

# Create your views here.
def Pizza_Sifaris(request):
    elave=Elave_sifaris()
    sifaris=Sifaris_Form(request.POST or None)
    if sifaris.is_valid():
        sifaris.save()

    return render(request,'form.html',{'sifaris':sifaris,'elave':elave})


def Ana_Seyfe(request):
    return render(request,'ev')

def Pizzalar(request):
    #formdaki reqedmi burax daxil etmek
    piazza_reqedm =2
    doldurulmus_pizza_form=Elave_sifaris(request.GET)
    if doldurulmus_pizza_form.is_valid():
        piazza_reqedm=doldurulmus_pizza_form.cleaned_data['reqem']
    pizza_form_set=formset_factory(Sifaris_Form ,extra=piazza_reqedm)
    #burda bitir
    formset=pizza_form_set()
    if request.method=='POST':
        filled_formset=pizza_form_set(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['terkibi'])
                filled_formset.save()
            note='Pizza sifarisi yaradildi'
        else:
            note ='Sifaris ugursuz oldu zehmet olmasa yeniden cehd edin'
        return render(request ,'form_set.html',{'note':note,'formset':formset})
    else:
        return render(request,'form_set.html',{'formset':formset})