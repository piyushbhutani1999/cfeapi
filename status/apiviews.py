from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .models import Status
from .serializers import StatusSerializer

class StatusListSearchAPIView(APIView):
    permission_classes =    []
    authentication_classes = []

    def get(self, request, format = None):
        qs = Status.objects.all()
        print(qs)
        serialize = StatusSerializer(qs, many = True)
        

        # print("SERIALIZED DATA : ", serialize.data)
        # [   
        #     OrderedDict([('user', 1), ('content', u'hellow world')]), 
        #     OrderedDict([('user', 1), ('content', u'this is second post')]), 
        #     OrderedDict([('user', 1), ('content', u'post number 3')])
        # ]

        return Response(serialize.data)


class StatusAPIView(ListAPIView):
    # all these are predefined , you just only have to add values to them
    # to make django know that what are you calling
    permission_classes = []
    authentication_classes = []
    queryset = Status.objects.all()
    serializer_class  = StatusSerializer


    def get_queryset(self):
        qs = Status.objects.all()

        # api/status/?q=ost
        # by this any object contains "ost" will be in qs
        # otherwise complete qs will be returned
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains = query)
        return qs
