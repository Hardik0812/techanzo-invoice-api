from django.contrib import admin
from invoice_details.models import Invoice,InvoiceDetails
# Register your models here.
admin.site.register(Invoice)
admin.site.register(InvoiceDetails)