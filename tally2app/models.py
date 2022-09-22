from audioop import ratecv
from codecs import BufferedIncrementalEncoder
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
    balance=models.IntegerField()
    types=models.CharField(max_length=10)
    
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
    amount=models.IntegerField()
    total_amount=models.IntegerField()

class journal(models.Model):
    no=models.AutoField(primary_key=True)
    no=models.IntegerField()
    particualrs=models.ForeignKey(ledger,on_delete=models.CASCADE,null=True)
    debit=models.IntegerField()
    credit=models.IntegerField()
    debit1=models.IntegerField()
    credit1=models.IntegerField()

class ledgercreation(models.Model):
  name=models.CharField(max_length=255,null=True)
  alias=models.CharField(max_length=255,null=True)
  under=models.CharField(max_length=255)
  bank_details=models.CharField(max_length=255,) 
  mname=models.CharField(max_length=255,null=True)
  address=models.CharField(max_length=255,null=True)
  country=models.CharField(max_length=255,null=True)
  state=models.CharField(max_length=255,null=True)
  pincode =models.IntegerField(null=True)
  pan_no =models.IntegerField(null=True)
  registration_type =models.CharField(max_length=255,null=True)
  gst_uin =models.IntegerField(null=True)
  set_alter_gstdetails =models.CharField(max_length=255,null=True)

  


  ac_holder_nm =models.CharField(max_length=255,null=True)
  acc_no =models.IntegerField(null=True) 
  ifsc_code =models.IntegerField(null=True)
  swift_code =models.IntegerField(null=True)
  bank_name =models.CharField(max_length=255,null=True) 
  branch =models.CharField(max_length=255,null=True)
  SA_cheque_bk =models.CharField(max_length=255,null=True)
  Echeque_p =models.CharField(max_length=255,null=True)

  occ_set_odl = models.CharField(max_length=255,null=True)
  occ_ac_holder_nm =models.CharField(max_length=255,null=True)
  occ_acc_no =models.IntegerField(null=True) 
  occ_ifsc_code =models.IntegerField(null=True)
  occ_swift_code =models.IntegerField(null=True)
  occ_bank_name =models.CharField(max_length=255,null=True) 
  occ_branch =models.CharField(max_length=255,null=True)
  occ_SA_cheque_bk =models.CharField(max_length=255,null=True)
  occ_Echeque_p =models.CharField(max_length=255,null=True)

  od_set_odl = models.CharField(max_length=255,null=True)
  od_ac_holder_nm =models.CharField(max_length=255,null=True)
  od_acc_no =models.IntegerField(null=True) 
  od_ifsc_code =models.IntegerField(null=True)
  od_swift_code =models.IntegerField(null=True)
  od_bank_name =models.CharField(max_length=255,null=True) 
  od_branch =models.CharField(max_length=255,null=True)
  od_SA_cheque_bk =models.CharField(max_length=255,null=True)
  od_Echeque_p =models.CharField(max_length=255,null=True)

  

  statutory_details=models.CharField(max_length=255,null=True)

  type_of_ledger = models.CharField(max_length=100,null=True)
  rounding_method = models.CharField(max_length=100,null=True)
  rounding_limit = models.IntegerField(blank=True, null=True, default=None)
  GST_Applicable = models.CharField(max_length=100,null=True)
  Alter_GST_Details= models.CharField(max_length=100,null=True)
  Appropriate=models.CharField(max_length=100,null=True)
  Types_of_supply=models.CharField(max_length=100,null=True)

  type_duty_tax = models.CharField(max_length=100,null=True)
  tax_type = models.CharField(max_length=100,null=True)
  percentage_of_calcution = models.CharField(max_length=100,null=True)
  rond_method = models.CharField(max_length=100,null=True)
  rond_limit = models.IntegerField(blank=True, null=True, default=None)

  balance_billbybill = models.CharField(max_length=100,null=True)
  credit_period = models.CharField(max_length=100,null=True)
  creditdays_voucher = models.CharField(max_length=100,null=True)

  def _str_(self):
        return self.name 


