from django.db import models

# Create your models here.

# Creating table with subject, msg and create date fields.
class Notice(models.Model):
    subject = models.CharField(max_length = 100)
    msg = models.TextField()
    cr_date = models.DateTimeField(auto_now_add = True)

class Student(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
