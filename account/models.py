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
    student = models.BooleanField(default =False)
    advertiser = models.BooleanField(default =False)
    date_created = models.DateTimeField(auto_now_add=True)
    city = models.ForeignKey(City, on_delete = models.DO_NOTHING)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return str(self.email)
