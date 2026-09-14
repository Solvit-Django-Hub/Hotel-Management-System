from django.db import models
from booking.models import Booking

class CheckIn(models.Model):
    id= models.BigAutoField(auto_created=True, unique=True, serialize=False, primary_key=True, verbose_name='ID')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    checkin_time = models.DateTimeField(auto_now_add=True)
    checked_in_by = models.CharField(max_length=30)
    notes= models.TextField(blank=True, null=True)
# Create your models here.
