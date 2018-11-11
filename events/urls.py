from django.urls import path
from .views import HomePageView, county_dataset


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('counties/', county_dataset, name='counties'),
]
