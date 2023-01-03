from django.contrib import admin
from .models import producto

# Register your models here.

class productosAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(producto)