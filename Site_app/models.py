from django.db import models
from django.contrib.auth.models import User

class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    score = models.IntegerField(default= 0)

    def __str__(self):
        return self.get_full_name()
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

class Forum(models.Model):
    text = models.CharField(max_length=500)  
    date_added = models.DateTimeField(auto_now_add=True)  
    user_name = models.CharField(max_length=50) 

    def __str__(self):
        return f'{self.text[:10]}, data:{self.date_added}, user:{self.user_name}'
    
