from django.shortcuts import render
from rest_framework import viewsets, permissions

from user import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
