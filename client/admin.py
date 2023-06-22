from django.contrib import admin
from .models import client, stats

# Register your models here.
admin.site.register(client),
admin.site.register(stats)