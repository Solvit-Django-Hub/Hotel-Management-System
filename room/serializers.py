from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'status', 'floor']
        read_only = ['room_id','is_active']