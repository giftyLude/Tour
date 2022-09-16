from django.contrib import admin
from .models import Lodge, Region, Site, Event

admin.site.register(Region)
admin.site.register(Site)
admin.site.register(Lodge)
admin.site.register(Event)
