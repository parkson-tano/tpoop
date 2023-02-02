from django.db import models
from location.models import City
from account.models import User
# Create your models here.
class House(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=256, null=True, blank=True)
    quater = models.CharField(max_length=256, null=True, blank=True)
    house_type = models.CharField(max_length=256, null=True)
    room_nb = models.IntegerField(default=0)
    toilet_nb = models.IntegerField(default=0)
    kitchen_nb = models.IntegerField(default=0)
    image_1 = models.ImageField(
        upload_to='house', null=True, blank=True)
    image_2 = models.ImageField(
        upload_to='house', null=True, blank=True)
    image_3 = models.ImageField(
        upload_to='house', null=True, blank=True)
    image_4 = models.ImageField(
        upload_to='house', null=True, blank=True)
    image_5 = models.ImageField(
        upload_to='house', null=True, blank=True)
    image_6 = models.ImageField(
        upload_to='house', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner + " house"
