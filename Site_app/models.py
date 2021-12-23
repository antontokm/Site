from django.db import models

class Table(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
