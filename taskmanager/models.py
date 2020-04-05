from djongo import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    task_description = models.CharField(max_length=1000)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name


