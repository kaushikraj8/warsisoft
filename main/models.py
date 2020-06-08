from django.db import models
from  datetime import datetime

# Create your models here.
class  contactdetails(models.Model):
    name=models.CharField( max_length=100,blank=False)
    phone=models.CharField(max_length=10,blank=False)
    subjects=models.CharField(max_length=90,blank=False)
    time=models.DateTimeField(datetime.now())
    class meta:
        verbose_name_plural="contact_details"
    def __str__(self):
        return self.name
    
        
class  email_contact(models.Model):
    name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=256,blank=False)
    subject=models.CharField(max_length=100,blank=False)
    message=models.TextField(max_length=500,blank=False)
    date=models.DateTimeField(datetime.now())
    class meta:
        verbose_name_plural="email_contact"
    def __str__(self):
        return self.name
    
    
    