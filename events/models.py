from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager


class Events(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = GeoManager()

    def __str__(self):
        return self.name


class Counties(models.Model):
    county3_id = models.FloatField()
    county = models.CharField(max_length=20)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.county
