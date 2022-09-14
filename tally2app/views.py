
from django.urls import path
from .import views
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import  *

# Create your views here.
def home(request):
    return render(request,'base.html')
def payment(request):
    bak=bank.objects.all()
    con=payment.objects.all()
    led=ledger.objects.all()
    return render(request,'payment.html',{'bak':bak,'led':led,'con':con})
    
def contra(request):
    bak=bank.objects.all()
    # con=contra.objects.all()
    led=ledger.objects.all()
    return render(request,'contra.html',{'bak':bak,'led':led})

def purchase(request):
    bak=bank.objects.all()
    # con=contra.objecs.all()
    led=ledger.objects.all()
    return render(request,'purchase.html',{'bak':bak,'led':led})
def sales(request):
    bak=bank.objects.all()
    # con=contra.objects.all()
    led=ledger.objects.all()
    return render(request,'sales.html',{'bak':bak,'led':led})
def receipt(request):
    bak=bank.objects.all()
    # con=contra.objects.all()
    led=ledger.objects.all()
    return render(request,'receipt.html',{'bak':bak,'led':led})
def receipt2(request):
    return render(request,'receipt2.html')
def journal(request):
    return render(request,'journal.html')
def creditnote(request):
    return render(request,'creditnote.html')
def debitnote1(request):
    return render(request,'debitnote1.html')
def editcontra(request):
    return render(request,'editcontra.html')
def editpayment(request):
    return render(request,'editpayment.html')
def createvoucher1(request):
    return render(request,'createvoucher1.html')