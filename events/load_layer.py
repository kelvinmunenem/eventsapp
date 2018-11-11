import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties


counties_mapping = {
    'county3_id': 'COUNTY3_ID',
    'county': 'COUNTY',
    'geom': 'MULTIPOLYGON',
}

county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/County.shp'))


def run(verbose=True):
    lm = LayerMapping(Counties, county_shp, counties_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
