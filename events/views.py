from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Counties, Events
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance


class HomePageView(TemplateView):
    template_name = 'index.html'


def county_dataset(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type='json')


def eventsnearme(request):
    if request.method == 'POST':
        longitude = request.POST['longitude']
        latitude = request.POST['latitude']
        location = Point(longitude, latitude, srid=4326)
        eventsnear = serialize('geojson', Events.objects.annotate(distance=Distance('position', location)).order_by('distance').first())
        return HttpResponse(eventsnear, content_type='json')
