from django.conf.urls import url

from .apiview import (
    UpdateModelDetailAPI, 
    UpdateModelListAPIView
)

urlpatterns = [
    url(r'^$', UpdateModelListAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', UpdateModelDetailAPI.as_view()),
]
