from django.db import models

from currency.models import Currency
from customer.models import Customer

# Create your models here.
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=150)
    currency = models.ForeignKey(Currency,on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    date = models.DateField()
    note = models.TextField(max_length=1000)
    sgst = models.FloatField()
    cgst = models.FloatField()

    def __str__(self):
        return self.invoice_number 


class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    sr_no = models.IntegerField()
    description = models.TextField(max_length=1000)
    rate = models.FloatField()
    quantity = models.IntegerField()
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sr_no 