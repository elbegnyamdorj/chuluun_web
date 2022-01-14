from typing import final
from django.shortcuts import render
from .models import Web
from .serializer import WebSerializer
from operator import itemgetter
# Create your views here.

def prepare_html(lang_name):
    web = Web.objects.all()
    serializers = WebSerializer(web, many = True)
    data = [dict(i) for i in serializers.data]
    web_list = sorted(data, key=itemgetter('order_number'))
    en_html = [d[lang_name] for d in web_list]
    final_html_string = ''.join(en_html)
    return final_html_string

def homeEN(request):
    print(request.POST)
    return render(request,'index.html', {'list':'{% load static%}'+prepare_html('en_html')})  

def homeMN(request):
    return render(request,'index.html', {'list':'{% load static%}'+prepare_html('mn_html')})  

