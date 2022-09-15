from audioop import ratecv
from django.db import models

# Create your models here.
class Vouchertype(models.Model):
    vouchertype=models.CharField(max_length=255,null=True)

class groups(models.Model):
    group=models.CharField(max_length=225)


    def __str__(self):
     return self.group

class ledger(models.Model):
    group=models.ForeignKey(groups,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=225)
    
    def __str__(self):
     return self.name

class transactiontype(models.Model):
    transactiontype=models.CharField(max_length=225)


class account(models.Model):
     account=models.ForeignKey(ledger,on_delete=models.CASCADE,null=True)
     date=models.DateTimeField()

class Particulars(models.Model):
    particualrs=models.ForeignKey(ledger,on_delete=models.CASCADE,null=True)
    amount=models.IntegerField()


class contra(models.Model):
       no=models.AutoField(primary_key=True)
       particualrs=models.ForeignKey(ledger,on_delete=models.CASCADE,null=True)
       amount1=models.IntegerField()
       amount2=models.IntegerField()
       amount3=models.IntegerField()

class payment(models.Model):
      no=models.AutoField(primary_key=True)
      particualrs=models.ForeignKey(ledger,on_delete=models.CASCADE,null=True)
      amount1=models.IntegerField()
      amount2=models.IntegerField()
      amount3=models.IntegerField()

class bank(models.Model):
    ledger=models.ForeignKey(ledger,on_delete=models.CASCADE,null=True)
    transactiontype=models.ForeignKey(transactiontype,on_delete=models.CASCADE,null=True)
    instno=models.IntegerField()
    instdate=models.DateField()
    amount=models.ForeignKey(Particulars,on_delete=models.CASCADE,null=True)
    date=models.ForeignKey(account,on_delete=models.CASCADE,null=True)
    vouchertype=models.ForeignKey(Vouchertype,on_delete=models.CASCADE,null=True)
   
class receipt(models.Model):
    no=models.AutoField(primary_key=True)
    particualrs=models.ForeignKey(ledger,on_delete=models.CASCADE,null=True)
    amount1=models.IntegerField()
    amount2=models.IntegerField()
    amount3=models.IntegerField()
class sales(models.Model):
       no=models.AutoField(primary_key=True)
       particualrs=models.ForeignKey(ledger,on_delete=models.CASCADE,null=True)
       Partyname=models.CharField(max_length=255)
       salesledger=models.CharField(max_length=255)
       item=models.CharField(max_length=255)
       rate=models.IntegerField()
       quantity=models.IntegerField()
       amount=models.IntegerField()
       total_amount=models.IntegerField()
       

    
  
    
class purchase(models.Model):
    no=models.AutoField(primary_key=True)
    particualrs=models.ForeignKey(ledger,on_delete=models.CASCADE,null=True)
    invoiceno=models.IntegerField() 
    no=models.IntegerField()   
    partyname=models.CharField(max_length=225)
    purchaseledger=models.CharField(max_length=225)
    itemname=models.CharField(max_length=225)
    quantity=models.IntegerField() 
    rate=models.IntegerField()

class journal(models.Model):
    no=models.AutoField(primary_key=True)
    no=models.IntegerField()
    particualrs=models.ForeignKey(ledger,on_delete=models.CASCADE,null=True)
    debit=models.IntegerField()
    credit=models.IntegerField()
    debit1=models.IntegerField()
    credit1=models.IntegerField()



    