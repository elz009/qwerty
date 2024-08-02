from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import SimpleRouter

app_name = 'core'

router = SimpleRouter()

router.register(r'indicator', views.IndicatorViewSet)
router.register(r'metaData', views.MetaDataViewSet)
router.register(r'media', views.MediaViewSet)
router.register(r'news', views.NewsViewSet)
router.register(r'publication', views.PublicationViewSet)
router.register(r'usefulLinks', views.UseFullLinkViewSet)
router.register(r'workmodel', views.WorkModelViewSet)  

urlpatterns = [
    
    path('api/category/', include('category.urls')),
    path('', include(router.urls)),
]
