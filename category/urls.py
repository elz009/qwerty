from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter
from .views import UploadFileView, ExcelUploadView

app_name = 'category'

router = SimpleRouter()

# Регистрация существующих ViewSets
router.register(r'state', views.StateViewSet)
router.register(r'district', views.DistrictViewSet)
router.register(r'indicatorCategory', views.IndicatorCategoryViewSet)
router.register(r'indicatorSubCategory', views.IndicatorSubCategoryViewSet)
router.register(r'newsCategory', views.NewsCategoryViewSet)
router.register(r'image', views.ImageViewSet)
router.register(r'graph_category', views.GraphCategoryViewSet)
router.register(r'workmodel', views.WorkModelViewSet)  

urlpatterns = [
    path('', include(router.urls)),
    path('upload-file/', UploadFileView.as_view(), name='upload_file'),
    path('excel-upload/', ExcelUploadView.as_view(), name='excel_upload'),
]
