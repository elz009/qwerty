from django.shortcuts import render
from rest_framework import viewsets
from .models import WorkModel
from .serializers import WorkModelSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import pandas as pd
from .models import WorkModel
from .serializers import ExcelUploadSerializer
from rest_framework import serializers

from category import models, serializers

class UploadFileView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            df = pd.read_excel(file)
            for _, row in df.iterrows():
                data = {
                    'unit': row.get('unit'),
                    'category': row.get('category'),
                    'subCategory': row.get('subCategory'),
                    'dateStart': row.get('dateStart'),
                    'dateEnd': row.get('dateEnd'),
                    'accepted': row.get('accepted'),
                    'name': row.get('name'),
                    'graphCategory': row.get('graphCategory'),
                    'value': row.get('value'),
                    'color': row.get('color'),
                    'year': row.get('year'),
                    'district': row.get('district'),
                    'state': row.get('state'),
                    'isVerified': row.get('isVerified'),
                }
                serializer = WorkModelSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response({'status': 'File processed successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ExcelUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ExcelUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            # Обработка данных и сохранение в базе данных
            for _, row in df.iterrows():
                WorkModel.objects.create(
                    unit=row.get('unit'),
                    category=row.get('category'),
                    subCategory=row.get('subCategory'),
                    dateStart=row.get('dateStart'),
                    dateEnd=row.get('dateEnd'),
                    accepted=row.get('accepted'),
                    name=row.get('name'),
                    graphCategory=row.get('graphCategory'),
                    value=row.get('value'),
                    color=row.get('color'),
                    year=row.get('year'),
                    district=row.get('district'),
                    state=row.get('state'),
                    isVerified=row.get('isVerified')
                )
            return Response({'status': 'File uploaded and data saved'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer
    pagination_class = None


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.DistrictSerializerGet
        else:
            return serializers.DistrictSerializer


class IndicatorCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.IndicatorCategory.objects.all().order_by('id')
    serializer_class = serializers.IndicatorCategorySerializer
    pagination_class = None


class IndicatorSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.IndicatorSubCategory.objects.all().order_by('id')
    serializer_class = serializers.IndicatorSubCategorySerializer
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.IndicatorSubCategorySerializerGet
        else:
            return serializers.IndicatorSubCategorySerializer


class NewsCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.NewsCategory.objects.all()
    serializer_class = serializers.NewsCategorySerializer
    pagination_class = None


class ImageViewSet(viewsets.ModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer
    pagination_class = None


class GraphCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.GraphCategory.objects.all()
    serializer_class = serializers.GraphCategorySerializer
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return serializers.GraphCategorySerializerGet
        else:
            return serializers.GraphCategorySerializer


class WorkModelViewSet(viewsets.ModelViewSet):
    queryset = WorkModel.objects.all()
    serializer_class = WorkModelSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('unit', 'category', 'subCategory', 'year', 'district', 'state', 'isVerified')
    ordering_fields = '__all__'
    ordering = ['id']

class Meta:
    model = WorkModel
    fields = '__all__'