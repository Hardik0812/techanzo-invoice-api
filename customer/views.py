from django.shortcuts import render
from customer.models import Customer
from rest_framework import generics
from rest_framework.response import Response
from customer.serializers import CustomerSerializer
from rest_framework import status
# Create your views here.



class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
  

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CustomerSerializer(queryset, many=True)
        return Response({"customers": serializer.data, "success": True}, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CustomerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"customers": serializer.data, "success": True}, status=status.HTTP_201_CREATED)

        return Response({"error": serializer.errors, "success": False}, status=status.HTTP_400_BAD_REQUEST)

    

        