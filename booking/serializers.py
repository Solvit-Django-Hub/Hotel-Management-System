from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['room','guest','status','check_in_date','check_out_date','number_of_guests','total_amount']
        read_only= ['booking_id','created_at']