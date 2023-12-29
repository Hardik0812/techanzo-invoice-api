

def increment_invoice_number():
    last_invoice = Invoice.objects.all().order_by('id').last()
    if not last_invoice:
         return '01-22/23'
    invoice_no = last_invoice.invoice_no
    invoice_int = int(invoice_no.split('01-22/23')[-1])
    new_invoice_int = invoice_int + 1
    new_invoice_no = '01-22/23' + str(new_invoice_int)
    return new_invoice_no