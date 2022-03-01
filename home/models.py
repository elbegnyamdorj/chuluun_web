from datetime import datetime
from distutils.text_file import TextFile
from pyexpat import model
from typing import Text
from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField
from django.forms import DateTimeField

# Create your models here.


class Web(models.Model):
    section_name = CharField(max_length=40)
    en_html = TextField()
    mn_html = TextField()
    order_number = IntegerField()

    def __str__(self):
        return f"{self.section_name}, {self.order_number}"


class News(models.Model):
    title = TextField()
    body = TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.body}, {self.date}"


class SanalHuselt(models.Model):
    name = TextField()
    email = TextField()
    phone = TextField()
    message = TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.email}, {self.phone}, {self.message}, {self.date}"
