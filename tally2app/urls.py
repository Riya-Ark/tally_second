from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('Payment',views.Payment,name='Payment'),
    path('Contra',views.Contra,name='Contra'),
    path('Receipt',views.Receipt,name='Receipt'),
    path('receipt2',views.receipt2,name='receipt2'),
    path('purchase',views.purchase,name='purchase'),
    path('Journal',views. Journal,name='Journal'),
    path('sales',views.sales,name='sales'),
    path('creditnote',views.creditnote,name='creditnote'),
    path('debitnote1',views.debitnote1,name='debitnote1'),
    # path('editcontra',views.editcontra,name='editcontra'),
    path('editpayment/<int:id>',views.editpayment,name='editpayment'),
    path('createvoucher1',views.createvoucher1,name='createvoucher1'),
    
    

    
    
]
