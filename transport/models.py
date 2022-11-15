from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class transport(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField( max_length=150)
    logo = models.ImageField(upload_to='transport_logo',default="no_picture.png")
    transporter_id = models.CharField(max_length=50,blank=True)
    mobile_no = models.IntegerField(default= 9521446207)
    landline_no = models.IntegerField(default= 9521446207)
    email = models.CharField(max_length=150,default="admin@transport.com")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

class branches(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField( max_length=150)
    transport = models.ForeignKey(transport, on_delete=models.CASCADE)
    mobile_no = models.IntegerField(default= 9521446207)
    landline_no = models.IntegerField(default= 9521446207)
    email = models.CharField(max_length=150,default="admin@transport.com")
    transporter_id = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("branch detail", kwargs={"pk": self.pk})
