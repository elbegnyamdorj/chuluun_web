from django.contrib import admin
from .models import News, SanalHuselt, Web

admin.site.register(Web)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "body", 'date')


@admin.register(SanalHuselt)
class SanalHuseltAdmin(admin.ModelAdmin):
    list_display = ("name", "email", 'phone', 'message', 'date')
