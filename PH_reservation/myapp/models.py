# Create your models here.
from django.db import models


# Create your models here.

class Classroom(models.Model):
    category = models.CharField(max_length=30)
    classroom_name = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    energyEffciency = models.CharField(max_length=30)
    capacity = models.DecimalField(decimal_places=0, max_digits=2)
    
    
    class Meta:
        verbose_name_plural = "List of Classrooms"

    def __str__(self):
        return self.classroom_name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "List of Users"

    def __str__(self):
        return self.email
    



class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)

    classroom_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    energyEffciency = models.CharField(max_length=30)
    capacity = models.DecimalField(decimal_places=2, max_digits=6)

    class Meta:
        verbose_name_plural = "List of Books"
    def __str__(self):
        return self.email
