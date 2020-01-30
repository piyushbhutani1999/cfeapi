# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#importing from python
import json

from django.db import models
from django.conf import settings
from django.core.serializers import serialize
from django.http import JsonResponse

def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user = instance.user, filename = filename)

# Create your models here.

# inherited Queryset class of django
class UpdateQuerySet(models.QuerySet):
    def serialize(self):
        qs = self
        final_array = []
        # for obj in qs:
        #     final_array.append(obj.serialize())
        # # doesnot looks like json format
        # # print(final_array)-->['{"content": "updates 1", "user": 1}', '{"content": "updates 2", "user": 1}', '{"content": "updates 3", "user": 1}']
        # return final_array
        for obj in qs:
            struct = json.loads(obj.serialize())
            # print(struct) - -> {u'content': u'updates 1', u'user': 1}
            final_array.append(struct)
        json_list = json.dumps(final_array)
        
        # print(json_list) - ->
        # [   {"content": "updates 1", "user": 1}, 
        #     {"content": "updates 2", "user": 1},
        #     {"content": "updates 3", "user": 1}
        # ]
        return json_list
        


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

        #serialize takes list of objects 
        data = serialize("json", [self], fields = {'user', 'content'})

        # print(data) --> [{"model": "updates.updates", "pk": 1, "fields": {"user": 1, "content": "updates 1"}}]
        
        
        #convert json content to python list of dictionary
        struct_of_field = json.loads(data)
        # print struct_of_fields --> [{u'pk': 1, u'model': u'updates.updates', u'fields': {u'content': u'updates 1', u'user': 1}}]
        
        json_data = json.dumps(struct_of_field[0]['fields'])
        # print(json_data) --> {"content": "updates 1", "user": 1}

        # print(JsonResponse(struct_of_field[0]['fields'])) --> {"content": "updates 1", "user": 1}

        # print(serialize("json", struct_of_fields[0]['fields'])) --> WRONG
        # as serialise takes list of objects and it is a dictionery

        # returns only the useful part i.e. fields
        return json_data
