from typing import final
import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import SanalHuselt, Web, News
from .serializer import WebSerializer, NewsSerializer
from operator import itemgetter
# Create your views here.


def get_news():
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)

    sort = sorted(serializer.data, key=lambda i: i['id'], reverse=True)
    # return {'date': 'sda', 'title': 'neg ym', 'body': 'lorem'}
    for i in sort:
        datetime_str = i['date']
        # 2022-02-20T23:02:32.707167+08:00
        date_time_obj = datetime.datetime.fromisoformat(datetime_str)
        i['date'] = date_time_obj
    return(sort[:2])


def prepare_html(lang_name):
    web = Web.objects.all()
    serializers = WebSerializer(web, many=True)
    data = [dict(i) for i in serializers.data]
    web_list = sorted(data, key=itemgetter('order_number'))
    en_html = [d[lang_name] for d in web_list]
    final_html_string = ''.join(en_html)

    # news = News.objects.all().order_by('-id')[:10]
    # news_in_ascending_order = reversed(news)

    return final_html_string


def homeEN(request):
    print(request)
    return render(request, 'index.html', {'list': '{% load static%}'+prepare_html('en_html'), 'news_list': get_news()})


def homeMN(request):
    return render(request, 'index.html', {'list': '{% load static%}'+prepare_html('mn_html'), 'news_list': get_news()})


def team(request):
    pass


def news(request):
    print(request.build_absolute_uri())
    return render(request, 'news.html')


def mail(request):
    data = request.POST
    email = data['email']
    name = data['name']
    phone = data['phone']
    message = data['message']
    sanal = SanalHuselt(email=email, name=name, phone=phone, message=message)
    sanal.save()
    return HttpResponse('success')
