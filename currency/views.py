from django.shortcuts import render
from currency.models import Currency
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from currency.serializers import CurrencySerializer
# Create your views here.



class CurrencyList(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"currency": serializer.data, "success": True}, status=status.HTTP_200_OK)


