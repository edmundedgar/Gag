#!/usr/bin/env python
# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
    def __unicode__(self):
        return u"%s's profile" % self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)