from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Student(AbstractUser):
    # Add additional fields for the student
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username