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
def receipt(request):
    return render(request,'receipt.html')
def journal(request):
    return render(request,'journal.html')
def creditnote(request):
    return render(request,'creditnote.html')
def debitnote(request):
    return render(request,'debitnote.html')