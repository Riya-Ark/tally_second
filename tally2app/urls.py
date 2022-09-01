from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('payment',views.payment,name='payment'),
    path('contra',views.contra,name='contra'),
    path('receipt',views.receipt,name='receipt'),
    path('purchase',views.payment,name='purchase'),
    path('journal',views.journal,name='journal'),
    path('creditnote',views.creditnote,name='creditnote'),
    path('debitnote',views.debitnote,name='debitnote'),
    # path('editcontra',views.editcontra,name='editcontra'),
    # path('editpayment',views.editpayment,name='editpayment'),
    
    

    
    
]
