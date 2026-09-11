from django.db import models
from room.models import Room
from guest.models import Guest

class Booking(models.Model):
    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    CANCELLED = 'Cancelled'
    
    Status_choices = [
        (PENDING, 'Pending'),
        (CONFIRMED, 'Confirmed'),
        (CANCELLED, 'Cancelled'),
    ]   
    booking_id = models.BigAutoField(auto_created=True, unique=True, serializable=False, primary_key=True, verbose_name='ID')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Status_choices, default=PENDING)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_guests = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
