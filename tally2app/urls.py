from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('payment',views.payment,name='payment'),
    path('contra',views.contra,name='contra'),
    path('receipt',views.receipt,name='receipt'),
    path('purchase',views.purchase,name='purchase'),
    path('journal',views.journal,name='journal'),
     path('sales',views.sales,name='sales'),
    path('creditnote',views.creditnote,name='creditnote'),
    path('debitnote1',views.debitnote1,name='debitnote1'),
    # path('editcontra',views.editcontra,name='editcontra'),
    path('editpayment/<int:pk>',views.editpayment,name='editpayment'),
    path('createvoucher1',views.createvoucher1,name='createvoucher1'),
    
    

    
    
]
