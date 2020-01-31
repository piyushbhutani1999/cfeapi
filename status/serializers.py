from rest_framework import serializers
from .models import Status


# This is same as djangoFroms format
# Check out the similarity in forms and serializers

'''
Serializers convert data in json and also validate that
'''


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'user', 'content'
        ]
