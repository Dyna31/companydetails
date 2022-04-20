from django.db import models


# Create your models here.
class companydb(models.Model):
    abc=models.ImageField(upload_to='media',null=True,blank=False)
    name=models.CharField(max_length=200,null=True,blank=False)
    location=models.CharField(max_length=100,null=True,blank=False)
    number=models.IntegerField(null=True,blank=False)
    edit=models.ImageField(max_length=100,null=True,blank=False)

