from django.contrib.gis import admin

from markers.models import Marker


@admin.register(Marker)
class MarkerAdmin(admin.GISModelAdmin):
    list_display = ("name", "description", "location", "hyperlink")
    search_fields = ("name", "description")