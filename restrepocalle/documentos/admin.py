from django.contrib import admin

# Register your models here.
from .models import  *


class ArchivoAdmin(admin.ModelAdmin):
    list_display=['fecha','tipo','cliente','image','observaciones']
    search_fields=["image"]
    list_filter=['fecha','tipo__nombreD','cliente__nombreC']



admin.site.register(Archivo, ArchivoAdmin)


admin.site.register(Cliente)
admin.site.register(Documento)

