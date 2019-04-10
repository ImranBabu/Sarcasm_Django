from django.db import models

class Register(models.Model):
    name = models.CharField(max_length=500)
    pwd = models.CharField(max_length=500)
    mailid = models.CharField(max_length=500)
    ph = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Comments(models.Model):
    feed = models.CharField(max_length=500)
    spam = models.CharField(max_length=10)

# Create your models here.
