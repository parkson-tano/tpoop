from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext as _
from location.models import City

class User(AbstractUser):
    username = models.CharField(
        max_length=50, blank=True, null=True, unique=False, default="")
    email = models.CharField(
        _('email'), unique=True, max_length=15)
    phone_number = models.CharField(
        _('phone_number'), unique=True, max_length=15)
    student = models.BooleanField(default =False)
    advertiser = models.BooleanField(default =False)
    date_created = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=256, null=True, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return str(self.email)


class PhoneNumber(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    phone = models.BigIntegerField(default=0)
    
    def __str__(self):
        return str(self.phone)
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        PhoneNumber.objects.create(user=instance, phone = instance.phone_number)


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.phonenumber.save()


