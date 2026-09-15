from django.db import models
from booking.models import Booking

class CheckOut(models.Model):
    id= models.BigAutoField(auto_created=True, unique=True, serialize=False, primary_key=True, verbose_name='ID')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    checkout_time = models.DateTimeField(auto_now_add=True)
    checked_out_by = models.CharField(max_length=30)
    extra_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True, null=True)

# Create your models here.
