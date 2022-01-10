from django.db import models

class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.get_full_name()
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
