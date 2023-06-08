from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField()
    description = models.CharField(max_length = 1000, default='')
    
    def __str__(self):
        return self.name
    
class Booking(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    comments = models.CharField(max_length = 1000)
    guest_number = models.IntegerField()
    
    def __str__(self):
        return self.first_name