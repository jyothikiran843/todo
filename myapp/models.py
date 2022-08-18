from django.utils import timezone,timesince
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tasks(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    deadline=models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

