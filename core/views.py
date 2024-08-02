from django.shortcuts import render
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import WorkModel 
from .serializers import WorkModelSerializer

from core import models, serializers, filters


class IndicatorViewSet(viewsets.ModelViewSet):
    queryset = models.Indicator.objects.all()
    serializer_class = serializers.IndicatorSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = filters.IndicatorFilter

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.IndicatorSerializerGet
        else:
            return serializers.IndicatorSerializer


class MetaDataViewSet(viewsets.ModelViewSet):
    queryset = models.MetaData.objects.all()
    serializer_class = serializers.MetaDataSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = filters.MetaDataFilter

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.MetaDataSerializerGet
        else:
            return serializers.MetaDataSerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = models.Media.objects.all().order_by('-ordering')
    serializer_class = serializers.MediaSerializer


class NewsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.NewsSerializerGet
        else:
            return serializers.NewsSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = models.Publication.objects.all()
    serializer_class = serializers.PublicationSerializer


class UseFullLinkViewSet(viewsets.ModelViewSet):
    queryset = models.UsefulLinks.objects.all()
    serializer_class = serializers.UsefulLinksSerializer


class WorkModelViewSet(viewsets.ModelViewSet):
    queryset = WorkModel.objects.all()
    serializer_class = WorkModelSerializer 