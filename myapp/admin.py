from django.contrib import admin
from .models import MainContactModel
from mapbox_location_field.admin import MapAdmin


admin.site.register(MainContactModel, MapAdmin)

