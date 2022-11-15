from django.db import models

# Create your models here.
class donation_items(models.Model):
    username=models.CharField(null=True,max_length=30)
    first_name=models.CharField(null=True,max_length=30)
    last_name=models.CharField(null=True,max_length=30)
    email_id=models.EmailField(null=True,max_length = 254)
    password=models.CharField(null=True,max_length=30)
    mobile_no=models.CharField(max_length=12)
    address=models.TextField() 