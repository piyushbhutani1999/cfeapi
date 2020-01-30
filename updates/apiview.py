import json
from .models import Updates
from django.http import HttpResponse
from django.views.generic import View
from .mixins  import CSRFExemptMixin
from .forms import UpdateModelForm

class UpdateModelDetailAPI(CSRFExemptMixin ,View):

    def get(self, request, id, *args, **kwargs):
        obj = Updates.objects.get(id = id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type = 'application/json')
    
    def post(self, request, *args, **kwargs):

        return HttpResponse({}, content_type='application/json') 
    
    def put(self, request, *args, **kwargs):

        return HttpResponse({}, content_type='application/json') 

    def delete(self, request, *args, **kwargs):

        return HttpResponse({}, content_type='application/json') 

class UpdateModelListAPIView(CSRFExemptMixin ,View):

    def get(self, request, *args, **kwargs):
        qs = Updates.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit= True)
            obj_data = obj.serialize()
            return HttpResponse(obj_data, content_type='application/json', status = 201)
        else:
            return HttpResponse(json.dumps(form.errors), content_type='application/json', status = 404)
