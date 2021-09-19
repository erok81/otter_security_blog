from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import HTModel


class HTModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(HTModel, HTModelAdmin)



