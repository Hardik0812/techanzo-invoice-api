from django.urls import path
from invoice_details.views import InvoiceDetailsList,InvoiceView,GetInvoiceView

urlpatterns = [
    path('invoice-details/', InvoiceDetailsList.as_view(), name='invoice-details-list'),
    path('invoice-details/<pk>/', InvoiceDetailsList.as_view(), name='invoice-details-delete'),
    path('add-invoice/',InvoiceView.as_view(),name="add-invoice"),
    path('get-invoice/<pk>/',GetInvoiceView.as_view(),name="get-invoice")
]