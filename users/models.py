from email.policy import default
from django.db import models

# Create your models here.

from django.contrib.auth.models import User

def get_user():
    return User.objects.get(id=1)

class donor_table(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=get_user)
    mobile_no=models.CharField(max_length=12)
    address=models.TextField() 
    profile_photo=models.ImageField(upload_to='iimages',null=True)

    def __str__(self):
        return self.user.username

class volunteer_table(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default=get_user)
    idpic=models.FileField(null=True)
    status=models.CharField(max_length=20, null=True)
    mobile_no=models.CharField(max_length=12,null=True)
    address=models.TextField() 

    def __str__(self):
        return self.user.username


class donate_items_details(models.Model):
    item_name=models.CharField(max_length=20, null=True)
    item_type=models.CharField(max_length=20, null=True)
    item_image=models.ImageField(upload_to='images',null=True)
    item_desc=models.CharField(max_length=200,null=True)
    donor_username=models.CharField(max_length=12,null=True)
    donor_mobile_no=models.CharField(max_length=12,null=True)
    donor_address=models.TextField() 
    volunteer_username=models.CharField(max_length=12,null=True)
    volunteer_mobile_no=models.CharField(max_length=12,null=True)
    volunteer_address=models.TextField() 

    def __str__(self):
        return self.item_name


class post_items_details(models.Model):
    item_name=models.CharField(max_length=20, null=True)
    item_type=models.CharField(max_length=20, null=True)
    item_desc=models.CharField(max_length=200,null=True)
    donor_username=models.CharField(max_length=12,null=True)
    donor_mobile_no=models.CharField(max_length=12,null=True)
    donor_address=models.TextField() 
    volunteer_username=models.CharField(max_length=12,null=True)
    volunteer_mobile_no=models.CharField(max_length=12,null=True)
    volunteer_address=models.TextField() 

    def __str__(self):
        return self.item_name