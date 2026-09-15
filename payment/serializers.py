from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [ 'booking', 'amount', 'payment_method', 'payment_status', 'payment_time', 'transaction_reference']
        read_only = ['id']