from django.db import models

# Create your models here.
class Tasks(models.Model):
    task = models.CharField(max_length=255)
    desc = models.TextField(max_length=1000)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task} {self.desc} {self.status}'