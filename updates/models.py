# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user = instance.user, filename = filename)

# Create your models here.
class Updates(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    content     = models.TextField()
    image       = models.ImageField(upload_to = upload_update_image, blank=True, null=True )
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content or ""