from rest_framework import serializers
from .models import Checkout

class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = ['booking','checked_out_by','extra_charges','notes']
        read_only= ['id','checkout_time']