# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Status
from .forms import StatusForm

class StatusAdmin(admin.ModelAdmin):
    # predefined keywords in django
    list_display = ['user', 'content']
    # if i use listdisplay = ['user', 'content'] it will not work

    form  = StatusForm



admin.site.register(Status, StatusAdmin)