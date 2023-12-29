from django.shortcuts import render
from invoice_details.models import InvoiceDetails,Invoice
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from invoice_details.serializers import InvoiceDetailsSerializer,InvoiceSerializer
from rest_framework import status
# Create your views here.



class InvoiceDetailsList(generics.ListCreateAPIView):
    queryset = InvoiceDetails.objects.all()
    serializer_class = InvoiceDetailsSerializer
  

    def list(self, request):
        queryset = self.get_queryset()
        serializer = InvoiceDetailsSerializer(queryset, many=True)
        return Response({"details": serializer.data, "success": True}, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = InvoiceDetailsSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"customers": serializer.data, "success": True}, status=status.HTTP_201_CREATED)

        return Response({"error": serializer.errors, "success": False}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        instance_id = kwargs.get('pk')
        if instance_id:
            try:
                instance = InvoiceDetails.objects.get(pk=instance_id)
                instance.delete()
                return Response({"success": True, "message": "Invoice details deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
            except InvoiceDetails.DoesNotExist:
                return Response({"success": False, "error": "Invoice details not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"success": False, "error": "Invalid request, provide a valid invoice details ID"}, status=status.HTTP_400_BAD_REQUEST)
        

class InvoiceView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = InvoiceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"invoice": serializer.data, "success": True}, status=status.HTTP_201_CREATED)

        return Response({"error": serializer.errors, "success": False}, status=status.HTTP_400_BAD_REQUEST)


class GetInvoiceView(RetrieveAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"invoice": serializer.data, "success": True}, status=status.HTTP_200_OK)