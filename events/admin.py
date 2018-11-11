from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Events,Counties


class EventsAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')


class Countiesadmin(LeafletGeoAdmin):
    list_display = ('county', )


admin.site.register(Events, EventsAdmin)
admin.site.register(Counties, Countiesadmin)
