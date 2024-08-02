from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path
from .models import WorkModel, State, District, IndicatorCategory, IndicatorSubCategory, NewsCategory, Image, GraphCategory
from .forms import ExcelUploadForm
import pandas as pd

class WorkModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'subCategory', 'dateStart', 'dateEnd', 'isVerified')
    search_fields = ('name', 'category', 'subCategory')
    list_filter = ('isVerified', 'dateStart', 'dateEnd')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-excel/', self.admin_site.admin_view(self.upload_excel), name='upload-excel'),
        ]
        return custom_urls + urls

    def upload_excel(self, request):
        if request.method == 'POST':
            form = ExcelUploadForm(request.POST, request.FILES)
            if form.is_valid():
                file = form.cleaned_data['file']
                data = pd.read_excel(file)
                data['dateStart'] = pd.to_datetime(data['dateStart'])
                data['dateEnd'] = pd.to_datetime(data['dateEnd'])
                data['isVerified'] = data['isVerified'].astype(bool)

                for index, row in data.iterrows():
                    WorkModel.objects.create(
                        unit=row['unit'],
                        category=row['category'],
                        subCategory=row['subCategory'],
                        dateStart=row['dateStart'],
                        dateEnd=row['dateEnd'],
                        accepted=row['accepted'],
                        name=row['name'],
                        graphCategory=row['graphCategory'],
                        value=row['value'],
                        color=row['color'],
                        year=row['year'],
                        district=row['district'],
                        state=row['state'],
                        isVerified=row['isVerified']
                    )
                self.message_user(request, "Excel файл успешно загружен")
                return redirect('..')
        else:
            form = ExcelUploadForm()
        
        context = {
            'form': form,
        }
        return render(request, 'admin/upload_excel.html', context)

# Регистрация моделей
admin.site.register(State)
admin.site.register(District)
admin.site.register(IndicatorCategory)
admin.site.register(IndicatorSubCategory)
admin.site.register(NewsCategory)
admin.site.register(Image)
admin.site.register(GraphCategory)
admin.site.register(WorkModel, WorkModelAdmin)
