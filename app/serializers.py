from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        models = React
        fields = ['employee', 'department']