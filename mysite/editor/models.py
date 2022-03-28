from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, default="user")
    password = models.CharField(max_length=32, default="changeme")
    address = models.CharField(max_length=80, default="noaddress")
    phone_number = models.IntegerField(11, default=87777777777)


class Image(models.Model):
    sku = models.CharField(max_length=32, default="null")
    url = models.TextField(
        max_length=255, default="https://zhana-aygerim.kz/404-not-found"
    )
    name = models.TextField(default="untitled")
    category = models.TextField(default="-")


class Order(models.Model):
    customer = models.CharField(max_length=255, blank=False, default="")
    customer_telephone = models.CharField(max_length=255, blank=False, default="")
    height = models.FloatField(default=0.0)
    width = models.FloatField(default=0.0)
    # fullsize_img = models.ForeignKey(Image, on_delete=models.CASCADE)
    preview = models.TextField(default="https://zhana-aygerim.kz/404-not-found")
    crop_data = models.IntegerField(default=0)
    styles = models.TextField(default="styles:none")
    status = models.IntegerField(default=0)
