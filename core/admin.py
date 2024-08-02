from django.contrib import admin
from core import models
from .models import WorkModel

admin.site.register(models.Indicator)
admin.site.register(models.MetaData)
admin.site.register(models.Media)
admin.site.register(models.News)
admin.site.register(models.Publication)
admin.site.register(models.UsefulLinks)
admin.site.register(WorkModel)