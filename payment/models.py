from django.db import models
from booking.models import Booking

class Payment(models.Model):
    CASH = 'Cash'
    CARD = 'Card'
    MOBILE_MONEY = 'Mobile Money'
    
    Method_choices = [
        (CASH, 'Cash'),
        (CARD, 'Card'),
        (MOBILE_MONEY, 'Mobile Money')
    ]
    PENDING = 'Pending'
    PAID = 'Paid'
    REFUNDED = 'Refunded'
    
    Payment_status_choices = [
        (PENDING, 'Pending'),
        (PAID, 'Paid'),
        (REFUNDED, 'Refunded')
    ]
    
    id= models.BigAutoField(auto_created=True, unique=True, serialize=False, primary_key=True, verbose_name='ID')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=Method_choices)
    payment_status = models.CharField(max_length=20, choices=Payment_status_choices, default=PENDING)
    payment_time = models.DateTimeField(auto_now_add=True)
    transaction_reference = models.CharField(max_length=50, unique=True)

# Create your models here.
