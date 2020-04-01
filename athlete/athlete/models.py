from django.db import models


# from django.forms import ModelForm
# Create your models here.


class StudentModel(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    stu_id = models.IntegerField()






