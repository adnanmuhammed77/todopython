from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=250)
    priority=models.IntegerField()
    date=models.DateField(default='1976-04-03')
    def __str__(self) -> str:
        return self.name