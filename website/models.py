from django.db import models
import datetime
# Create your models here.

class admin_account(models.Model):
    Admin_ID = models.BigAutoField(primary_key=True)
    Admin_Name = models.CharField(max_length=255)
    Admin_Email = models.EmailField(max_length=255)
    Admin_User = models.CharField(max_length=255)
    Admin_Password = models.CharField(max_length=255)
    Admin_Phone = models.IntegerField()

class client(models.Model):
    Client_ID = models.BigAutoField(primary_key=True)
    #Client_ID_Number = models.ForeignKey()
    
#class client_account(models.Model):
    
#class client_transaction(models.Model):
    
#class inventory(models.Model):

#class archive(models.Model):

#class faqs(models.Model):