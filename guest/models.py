from django.db import models

class Guest(models.Model):
    guest_id = models.BigAutoField(auto_created=True, unique=True, serialize=False, primary_key=True, verbose_name='Guest ID')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=10)
    address = models.TextField(max_length=50)
    date_of_birth = models.DateField()
    
# Create your models here.
