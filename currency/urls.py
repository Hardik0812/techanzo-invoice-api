from django.urls import path
from currency.views import CurrencyList

urlpatterns = [
    path('currencies/', CurrencyList.as_view(), name='currency-list'),
]