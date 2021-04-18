from django.db import models


class Hathway(models.Model):
    email = models.EmailField(null=True, blank=True)
    url = models.URLField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.email


class Employee(models.Model):
    name = models.CharField(primary_key=True, max_length=500, blank=True)
    dob = models.DateField()
    age = models.IntegerField()
    address = models.TextField()
    professsion = models.CharField(max_length=40, null=True, blank=True)
    hathway = models.ForeignKey(Hathway, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Unlimited(models.Model):
    name = models.ManyToManyField(Employee)
    speed = models.IntegerField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.location
# Create your models here.
