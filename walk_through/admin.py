from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import WKModel


class WKModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(WKModel, WKModelAdmin)
