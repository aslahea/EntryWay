from django.contrib.auth.models import AbstractUser 
from django.db import models

GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
]

class CustomUser(AbstractUser) :
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    is_deleted = models.BooleanField(default=False)

    def __str__ (self):
        return str(self.username or "")    
    

   


