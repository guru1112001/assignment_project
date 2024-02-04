from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField()
    date_of_birth=models.DateField()

    def __str__(self):
        return self.name