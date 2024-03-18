from django.db import models

# Create your models here.
class Register(models.Model):
    Id = models.AutoField
    First_Name = models.CharField(max_length=60)
    Last_Name = models.CharField(max_length=60)
    Mobile = models.CharField(max_length=60)
    Email = models.CharField(max_length=60)
    Password = models.CharField(max_length=60)
    DOB = models.DateField()

    def __str__(self):
        return self.First_Name


class RoomAllocation(models.Model):
    Id = models.AutoField
    Room_Type = models.CharField(max_length=60)
    AC_NON_AC = models.CharField(max_length=60)
    Mobile = models.CharField(max_length=60)
    Email = models.CharField(max_length=60)
    Password = models.CharField(max_length=60)
    DOB = models.DateField()

    def __str__(self):
        return f'{self.Room_Type}-{self.Mobile}-{self.AC_NON_AC}'
