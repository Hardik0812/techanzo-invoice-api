from rest_framework import serializers
from datetime import datetime
from invoice_details.models import InvoiceDetails, Invoice
from currency.models import Currency
from customer.models import Customer
# class InvoiceDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InvoiceDetails
#         fields = "__all__"

# class InvoiceSerializer(serializers.ModelSerializer):
#     date = serializers.DateField(input_formats=["%d/%m/%Y"], format="%d/%m/%Y")
#     created_at = serializers.CharField(required=False)
#     updated_at = serializers.CharField(required=False)

#     def get_invoice_details(self, instance):
#         details = {
#             "total_amount": instance.sgst + instance.cgst,  
#         }
#         return details

#     class Meta:
#         model = Invoice
#         fields = [
#             "id",
#             "invoice_number",
#             "currency",
#             "customer",
#             "date",
#             "note",
#             "sgst",
#             "cgst",
#             "created_at",
#             "updated_at",
#         ]

#     def to_representation(self, instance):
#         # Use the parent class to_representation method
#         ret = super().to_representation(instance)

#         # Check if the request is a GET request
#         if self.context.get('request') and self.context['request'].method == 'GET':
#             # Add additional details using InvoiceDetailsSerializer
#             details_queryset = InvoiceDetails.objects.filter(invoice=instance)
#             details_serializer = InvoiceDetailsSerializer(details_queryset, many=True)
#             ret['invoice_details'] = details_serializer.data
#         else:
#             # For other request methods (POST, etc.), use the custom method
#             ret['invoice_details'] = self.get_invoice_details(instance)

#         return ret

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'name']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name']

class InvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetails
        fields = "__all__"

class InvoiceSerializer(serializers.ModelSerializer):
    date = serializers.DateField(input_formats=["%d/%m/%Y"], format="%d/%m/%Y")
    created_at = serializers.CharField(required=False)
    updated_at = serializers.CharField(required=False)

    currency = CurrencySerializer()
    customer = CustomerSerializer()

    def get_invoice_details(self, instance):
        details = {
            "total_amount": instance.sgst + instance.cgst,  
        }
        return details

    class Meta:
        model = Invoice
        fields = [
            "id",
            "invoice_number",
            "currency",
            "customer",
            "date",
            "note",
            "sgst",
            "cgst",
            "created_at",
            "updated_at",
        ]

    def to_representation(self, instance):
        # Use the parent class to_representation method
        ret = super().to_representation(instance)

        # Check if the request is a GET request
        if self.context.get('request') and self.context['request'].method == 'GET':
            # Add additional details using InvoiceDetailsSerializer
            details_queryset = InvoiceDetails.objects.filter(invoice=instance)
            details_serializer = InvoiceDetailsSerializer(details_queryset, many=True)
            ret['invoice_details'] = details_serializer.data

            # Add currency details
            currency_serializer = CurrencySerializer(instance.currency)
            ret['currency'] = currency_serializer.data

            # Add customer details
            customer_serializer = CustomerSerializer(instance.customer)
            ret['customer'] = customer_serializer.data

        else:
            # For other request methods (POST, etc.), use the custom method
            ret['invoice_details'] = self.get_invoice_details(instance)

        return ret
