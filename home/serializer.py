from dataclasses import field
from django.db import models
from rest_framework import serializers
from .models import SanalHuselt, Web, News


class WebSerializer(serializers.ModelSerializer):
    class Meta:
        model = Web
        fields = [
            'section_name',
            'en_html',
            'mn_html',
            'order_number'
        ]


class SanalHuseltSerializer(serializers.ModelSerializer):
    class Meta:
        model = SanalHuselt
        fields = [

            'name',
            'email',
            'phone',
            'message',
            'date',
        ]


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'id',
            'title',
            'body',
            'date'
        ]
