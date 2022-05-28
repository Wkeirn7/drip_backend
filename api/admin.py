from django.contrib import admin
from .models import Graph, Asset

# Register your models here.
admin.site.register([Graph, Asset])