from django.db import models

# Create your models here.
class Task(models.Model):
    task_name=models.CharField(max_length=250)
    task_description=models.TextField()
    task_time = models.DateTimeField(auto_now_add=True)
    task_iscompleted=models.BooleanField()

    def __str__(self):
        return self.task_name
