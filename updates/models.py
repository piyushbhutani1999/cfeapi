# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.db import models
from django.conf import settings
from django.core.serializers import serialize

def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user = instance.user, filename = filename)

# Create your models here.

# inherited Queryset class of django
class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        qs = self
        # since it is a class of queryset so it automatically updates
        # model in Updates.objects.all() i.e. list of objects
        return serialize("json", qs, fields = {'user', 'content'})


# it is a class which is used to update predefined functions of django
class UpdateManager(models.Manager):
    # predefined function which is used to get list of queryset
    def get_queryset(self):
        return UpdateQuerySet(self.model, using= self._db)


class Updates(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL)
    content     = models.TextField()
    image       = models.ImageField(upload_to = upload_update_image, blank=True, null=True )
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    # defing in model that its manager is Update Manager as we change
    # some builtin functions which it takes from that class
    # ALSO MEANS THAT NOW OBJECTS ARE BASED ON UPDATEMANAGER 
    # if we write obj = UpdateManager() then in view data = Updates.obj.all()
    objects = UpdateManager()

    def __str__(self):
        return self.content or ""
    
    #define a function here to serialse a single objects
    def serialize(self):
        # this function return this :
        # [ {
        #       "model": "updates.updates", 
        #       "pk": 1, 
        #       "fields": {"user": 1, "content": "updates 1"}
        #   }
        # ]
        # we dont need all these, we only need fields portion which is of our requirement
        data = serialize("json", [self], fields = {'user', 'content'})

        #convert json content to python list of dictionary

        struct_of_field = json.loads(data)
        #[{u'pk': 1, u'model': u'updates.updates', u'fields': {u'content': u'updates 1', u'user': 1}}]
        
        # returns only the useful part i.e. fields
        return struct_of_field[0]['fields']
