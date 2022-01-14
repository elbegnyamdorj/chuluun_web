from django.db import models
from rest_framework import serializers
from .models import Web


class WebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web
        fields = [
            'section_name',
            'en_html',
            'mn_html',
            'order_number'
        ]
    