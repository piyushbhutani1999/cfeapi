from django.conf.urls import url
from .apiviews import StatusListSearchAPIView, StatusAPIView

urlpatterns = [
    # url(r'^$', StatusListSearchAPIView.as_view()),
    url(r'^$', StatusAPIView.as_view()),
]
