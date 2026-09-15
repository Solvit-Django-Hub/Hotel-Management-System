from rest_framework import serializers
from .models import CheckIn

class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ['booking','checked_in_by','notes']
        read_only= ['id','check_in_time']