from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
TYPE_CHOICES = (
    ('Core', 'Core'),
    ('Legs', 'Legs'),
    ('Arms', 'Arms'),
    ('Chest', 'Chest'),
    ('Full-Body', 'Full-Body'),
)

class User(AbstractUser):
    pass

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    weight = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='Full-Body')
    cal_burn = models.FloatField(default=0.0)
    image = models.ImageField(upload_to="exercise/images", default="")
    desc = models.TextField()
    link = models.CharField(max_length=2000, null=False)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointment")
    full_name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=13)
    desc = models.TextField()
    address = models.TextField()
    pincode = models.CharField(max_length=6)
    timeStamp = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f'Message from {self.full_name}'


class Calorie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="appointment")
    calorie_burnt = models.FloatField(default=0.0)
    date = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.calorie_burnt