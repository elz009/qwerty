from django_filters import rest_framework as filters
from core import models
from django_filters import FilterSet


class IndicatorFilter(FilterSet):
    subCategory = filters.CharFilter('subCategory')
    graphCategory = filters.CharFilter('graphCategory')

    class Meta:
        models = models.Indicator
        fields = ('subCategory', 'graphCategory')


class MetaDataFilter(FilterSet):
    subCategory = filters.CharFilter('subCategory')

    class Meta:
        model = models.MetaData
        fields = ('subCategory', )
