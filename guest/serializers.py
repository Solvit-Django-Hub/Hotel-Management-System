from rest_framework import serializers
from .models import Guest

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth']
        read_only_fields = ['guest_id']