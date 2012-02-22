from words.models import Document
from django.contrib import admin
from django.contrib.admin import site, ModelAdmin

def sents(instance):
    return ', '.join(instance.sents)

class DocumentAdmin(ModelAdmin):
    list_display = ['title', sents]

admin.site.register(Document, DocumentAdmin)
