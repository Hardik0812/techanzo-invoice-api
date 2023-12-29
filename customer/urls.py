from django.urls import path
from customer.views import CustomerList

urlpatterns = [
    path('customers/', CustomerList.as_view(), name='customers-list'),
]