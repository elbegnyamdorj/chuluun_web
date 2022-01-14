from django.db import models
from django.db.models.fields import CharField, IntegerField, TextField

# Create your models here.
class Web(models.Model):
    section_name = CharField(max_length=40)
    en_html = TextField()
    mn_html = TextField()
    order_number = IntegerField()
    def __str__(self):
        return f"{self.section_name}, {self.order_number}"