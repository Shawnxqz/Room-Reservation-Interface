# Create your models here.
from django.db import models


# Create your models here.

class Classroom(models.Model):
    category = models.CharField(max_length=30)
    classroom_name = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    energyEfficiency = models.DecimalField(decimal_places=2, max_digits=5)
    capacity = models.DecimalField(decimal_places=0, max_digits=3)
    number_student = models.DecimalField(decimal_places=0, max_digits=3)
    noise = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "List of Classrooms"

    def __str__(self):
        return self.classroom_name


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    email = models.EmailField()
    andrewid = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    class Meta:
        verbose_name_plural = "List of Users"

    def __str__(self):
        return self.email
    



class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    CLASSROOM_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    # bookid = models.DecimalField(decimal_places=0, max_digits=2)
    email = models.EmailField()
    andrewid = models.CharField(max_length=30)
    userid = models.DecimalField(decimal_places=0, max_digits=2)

    classroom_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    book_status = models.CharField(choices=CLASSROOM_STATUSES, default=BOOKED, max_length=30)
    energyEfficiency = models.DecimalField(decimal_places=2, max_digits=5)
    capacity = models.DecimalField(decimal_places=0, max_digits=3)
    number_student = models.DecimalField(decimal_places=0, max_digits=3)
    shareRoom = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "List of Books"
    def __str__(self):
        return self.email
