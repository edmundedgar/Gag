#!/usr/bin/env python
# encoding: utf-8

from django.contrib import admin
from auth.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserProfile, UserProfileAdmin)