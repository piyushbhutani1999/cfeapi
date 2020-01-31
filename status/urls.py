from django.conf.urls import url
from .apiviews import (
    StatusListSearchAPIView, 
    StatusAPIView, 
    StatusACreatePIView,
    StatusDetailView,
    )


urlpatterns = [
    # url(r'^$', StatusListSearchAPIView.as_view()),
    url(r'^$', StatusAPIView.as_view()),
    url(r'^create/$', StatusACreatePIView.as_view()),
    url(r'^(?P<pk>.*)/$', StatusDetailView.as_view()),

]
