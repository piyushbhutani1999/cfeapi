# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

# Create your models here.


class StatusQuerySet(models.QuerySet):
    def serialize(self):
        qs = self
        final_array = []
        for obj in qs:
            struct = json.loads(obj.serialize())
            final_array.append(struct)
        json_list = json.dumps(final_array)
        return json_list


class StatusManager(models.Manager):
    # predefined function which is used to get list of queryset
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


def upload_status_image(instance, filename):
    return "Statuss/{user}/{filename}".format(user = instance.user, filename = filename)

class Status(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    content     = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to = upload_status_image, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content)
    
    objects = StatusManager()

    class Meta:
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'
