from django.db import models
from django.urls import reverse

class Course(models.Model):
    cname = models.CharField(max_length=30)
    duration = models.IntegerField()
    fee = models.IntegerField()


    def __str__(self):
        return self.cname
