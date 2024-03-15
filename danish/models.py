from django.db import models

class message_table(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    subject = models.CharField(max_length = 20)
    phone_n = models.CharField(max_length=15)
    message = models.CharField(max_length = 150)




class registration_table(models.Model):
    name = models.CharField(max_length = 20)
    fname = models.CharField(max_length = 20)
    dob = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length = 40)
    phone_n = models.CharField(max_length = 20)
    exp_skills = models.CharField(max_length = 30)
    information = models.CharField(max_length = 200)

# Create your models here.
