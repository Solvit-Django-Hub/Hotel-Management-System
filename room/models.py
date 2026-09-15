from django.db import models
from roomtype.models import RoomType

class Room(models.Model):
    AVAILABLE = 'Available'
    OCCUPIED = 'Occupied'
    MAINTENANCE = 'Maintenance'
    CLEANING = 'Cleaning'
    
    Status_choices = [
        (AVAILABLE, 'Available'),
        (OCCUPIED, 'Occupied'),
        (MAINTENANCE, 'Maintenance'),
        (CLEANING, 'Cleaning'),
    ]
    room_id = models.BigAutoField(auto_created=True, unique=True, serialize=False, primary_key=True, verbose_name='Room ID')
    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    floor = models.IntegerField()
    status = models.CharField(max_length=20, choices=Status_choices, default=AVAILABLE)
    is_active = models.BooleanField(default=True)

# Create your models here.
