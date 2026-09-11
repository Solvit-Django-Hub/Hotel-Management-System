from django.db import models

class RoomType(models.Model):
    roomtype_id = models.BigAutoField(auto_created=True, unique=True, serializable=True, primary_key=True, verbose_name='Room Type ID')
    roomtype_name = models.CharField(max_length=30)
    roomtype_description = models.TextField()
    roomtype_price = models.DecimalField(max_digits=10, decimal_places=2)
    roomtype_capacity = models.IntegerField()
    roomtype_amenities = models.TextField(max_length=255)

# Create your models here.
