from django.contrib import admin

from .models import *

admin.site.register(Client)
admin.site.register(FeatureRequest)
admin.site.register(ClientPriority)