# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Customers(models.Model):

    #__Customers_FIELDS__
    customer = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    officenumber = models.CharField(max_length=255, null=True, blank=True)
    company = models.TextField(max_length=255, null=True, blank=True)
    rep = models.TextField(max_length=255, null=True, blank=True)
    dateadded = models.DateTimeField(blank=True, null=True, default=timezone.now)
    lastvisiteddate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Customers_FIELDS__END

    class Meta:
        verbose_name        = _("Customers")
        verbose_name_plural = _("Customers")



#__MODELS__END
