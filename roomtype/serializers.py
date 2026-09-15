from rest_framework import serializers
from .models import RoomType

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['roomtype_name', 'roomtype_description', 'roomtype_price', 'roomtype_capacity', 'roomtype_amenities']
        read_only = ['roomtype_id']