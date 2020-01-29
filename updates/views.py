# -*- coding: utf-8 -*-
from __future__ import unicode_literals


#render is a shortcut to http templte response
# render(templateName, **CONTEXT**)
# render = HttpResponse(get_template().render({**CONTEXT**}))
from django.shortcuts import render 

# Create your views here.
from .models import Updates
from django.http import JsonResponse, HttpResponse


def update_models_detail_view(request):
    data = {
        "count" : 1000,
        "content" : "here comes content"
    }
    #JsonResponse convert python dict to JS objects notation(JSON)
    return JsonResponse(data)