# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# render is a shortcut to http templte response
# render(templateName, **CONTEXT**)
# render = HttpResponse(get_template().render({**CONTEXT**}))
from django.shortcuts import render 

from django.core.serializers import serialize

# Create your views here.
from .models import Updates
from django.http import JsonResponse, HttpResponse
from django.views.generic import View


def jsonExampleView(request):
    data = {
        "count" : 1000,
        "content" : "here comes content"
    }
    # JsonResponse convert python dict to JS objects notation(JSON)
    return JsonResponse(data)

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "countclass" : "class"
        }
        return JsonResponse(data)


# in this we cover a manual way of serialising the data
# but this is difficult in case we have to serialize a complete query set
# thats why we make serializer class
class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        # manual way of serialising the data
        obj = Updates.objects.get(it = 1)
        data = {
            "username" : obj.user.username,
            "content"  : obj.content
        }
        return JsonResponse(data)


class SerializeListView1(View):
    def get(self, request, *args, **kwargs):
        # manual way of serialising the data
        qs = Updates.objects.all()
        data = serialize("json", qs, fields = {'user', 'content'})
        print(data)
        # if we dont use content_type then data is pass as it is.
        # data is in json format but to let know the browser we pass contetn type
        # serialize convert our data to json
        return HttpResponse(data, content_type = 'application/json')
        # the data returned by this is this, but we dont need all the data..the data is not in good format.
        # [   
        #     {"model": "updates.updates", "pk": 1, "fields": {"user": 1, "content": "updates 1"}},  
        #     {"model": "updates.updates", "pk": 2, "fields": {"user": 1, "content": "updates 2"}}, 
        #     {"model": "updates.updates", "pk": 3, "fields": {"user": 1, "content": "updates 3"}}
        # ]


# It is another way of serialising queryset
class SerializeListView2(View):
    def get(self, request, *args, **kwargs):
        qs = Updates.objects.all()
        data = []
        for obj in qs:
            data.append(obj)
        print(data)
        data = serialize("json", data)
        # return JsonResponse(data) is wrong.. see next view 
        return HttpResponse(data, content_type = 'application/json')

# JsonResponse only accept dictionay instance
class SerializeListView(View):
    def get(self, request, *args, **kwargs):
        qs = Updates.objects.all()
        data = []
        for obj in qs:
            data.append(
                {
                    "username" : obj.user.username,
                    "content" : obj.content,
                }
            )
        #inorder to pass a non dict object set safe  =  false, bcz JsonResponse only accepts dictionary object
        return HttpResponse(JsonResponse(data, safe = False), content_type = 'application/json') 

