from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class Student(AbstractUser):        # This is form that we use for login page....
    # Add additional fields for the student
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
    #INSERT INTO Employee (T_Name, Designation, Username, Pass_word, Mobile_number, Email, DOB, Date_of_Joining)  
    
class Teacher(models.Model):
    T_name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Username = models.CharField(max_length=100, primary_key=True)
    Pass_word = models.CharField(max_length=100)
    Moblie_number = models.CharField(max_length=10)
    Email = models.EmailField(max_length=100)
    DOB = models.DateField()
    Date_of_Joining = models.DateField()
    #
    

    def __str__(self):
        return self.T_name
    
    #super user create : name: admin, password: pass