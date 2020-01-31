from django.conf.urls import url
from .apiviews import (
    StatusListSearchAPIView, 
    StatusAPIView, 
    StatusACreatePIView,
    StatusDetailView,
    StatusUpdateView,
    StatusDeleteView
    )


urlpatterns = [
    # url(r'^$', StatusListSearchAPIView.as_view()),
    url(r'^$', StatusAPIView.as_view()),
    url(r'^create/$', StatusACreatePIView.as_view()),
    url(r'^(?P<pk>.*)/$', StatusDetailView.as_view()),
    url(r'^(?P<pk>.*)/delete$', StatusDeleteView.as_view()),
    url(r'^(?P<pk>.*)/update$', StatusUpdateView.as_view()),

]
