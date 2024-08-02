from rest_framework import serializers
from category.models import WorkModel 

from category.serializers import IndicatorCategorySerializer, IndicatorSubCategorySerializer, NewsCategorySerializer, \
    GraphCategorySerializer
from core import models


class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Indicator
        fields = ('id', 'unit', 'category', 'subCategory', 'dateStart', 'dateEnd', 'accepted', 'name', 'graphCategory',
                  'value', 'color')


class IndicatorSerializerGet(serializers.ModelSerializer):
    category = IndicatorCategorySerializer()
    subCategory = IndicatorSubCategorySerializer()
    graphCategory = GraphCategorySerializer()

    class Meta:
        model = models.Indicator
        fields = ('id', 'unit', 'category', 'subCategory', 'dateStart', 'dateEnd', 'accepted', 'name', 'graphCategory',
                  'value', 'color')


class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MetaData
        fields = ('id', 'name', 'type', 'description', 'indicator', 'subCategory', 'icon', 'value')


class MetaDataSerializerGet(serializers.ModelSerializer):
    indicator = IndicatorSerializer()
    subCategory = IndicatorSubCategorySerializer()

    class Meta:
        model = models.MetaData
        fields = ('id', 'name', 'type', 'description', 'indicator', 'subCategory', 'icon', 'value')


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Media
        fields = ('id', 'ordering', 'image', 'title')


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ('id', 'type', 'title', 'description', 'link', 'datePublication', 'category')


class NewsSerializerGet(serializers.ModelSerializer):
    category = NewsCategorySerializer()

    class Meta:
        model = models.News
        fields = ('id', 'type', 'title', 'description', 'link', 'datePublication', 'category')


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publication
        fields = ('id', 'title', 'description', 'image', 'dateCreated')


class UsefulLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UsefulLinks
        fields = ('id', 'title', 'image', 'dateCreated')

class WorkModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkModel
        fields = '__all__'