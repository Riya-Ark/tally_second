
from django.urls import path
from .import views
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import  *

# Create your views here.
def home(request):
    return render(request,'base.html')
# def ledgercreation():
#     return render(request,'ledgercreation.html')

def Payment(request):
    
    bak=bank.objects.all()
    con=payment.objects.all()
    a=con.no+1
    led=ledger.objects.all()
    return render(request,'payment.html',{'bak':bak,'led':led,'con':con,'a':a})
    
def Contra(request):
    bak=bank.objects.all()
    con=contra.objects.all()
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
def Receipt(request):
    bak=bank.objects.all()
    re=receipt.objects.all()
    led=ledger.objects.all()
    return render(request,'receipt.html',{'bak':bak,'led':led,'re':re})
def receipt2(request):
    return render(request,'receipt2.html')
def Journal(request):
    bak=bank.objects.all()
    # con=contra.objects.all()
    led=ledger.objects.all()
    return render(request,'journal.html',{'bak':bak,'led':led})
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