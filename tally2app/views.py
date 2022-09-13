from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')
def payment(request):
    return render(request,'payment.html')
def contra(request):
    return render(request,'contra.html')
def purchase(request):
    return render(request,'purchase.html')
def sales(request):
    return render(request,'sales.html')
def receipt(request):
    return render(request,'receipt.html')
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