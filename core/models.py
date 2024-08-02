from django.db import models

from category.models import IndicatorCategory, IndicatorSubCategory, NewsCategory, GraphCategory
from core import utils


class Indicator(models.Model):
    class Meta:
        verbose_name = 'Индикатор'
        verbose_name_plural = 'Индикаторы'

    unit = models.CharField('Единица измерения', max_length=255)
    category = models.ForeignKey(IndicatorCategory, models.SET_NULL, null=True, blank=True, verbose_name='Категория')
    subCategory = models.ForeignKey(IndicatorSubCategory, models.SET_NULL, null=True, blank=True, verbose_name='Под категория')
    dateStart = models.DateField('Дата начала', blank=True)
    dateEnd = models.DateField('Дата окончания', blank=True)
    accepted = models.BooleanField('Принято', default=False)
    name = models.CharField('Название', max_length=255, blank=True)
    graphCategory = models.ForeignKey(GraphCategory, models.SET_NULL, null=True, blank=True, verbose_name='Категория графов')
    value = models.FloatField('Значение', default=0)
    color = models.CharField('Цвет', max_length=255, blank=True)

    def __str__(self):
        return str(self.unit)


class MetaData(models.Model):
    class Meta:
        verbose_name = 'Мета данные'
        verbose_name_plural = 'Мета данные'

    name = models.CharField('Название', max_length=255)
    type = models.CharField('Тип', max_length=255, blank=True)
    description = models.TextField('Описание', blank=True)
    indicator = models.ForeignKey(Indicator, models.SET_NULL, null=True, blank=True, verbose_name='Индикатор')
    subCategory = models.ForeignKey(IndicatorSubCategory, models.SET_NULL, null=True, blank=True,
                                    verbose_name='Под категория')
    icon = models.TextField('Иконка', blank=True)
    value = models.FloatField('Значение', default=0)

    def __str__(self):
        return str(self.name)


class Media(models.Model):
    class Meta:
        verbose_name = 'Медиа'
        verbose_name_plural = 'Медиа'

    ordering = models.IntegerField('Приоритет', default=0)
    image = models.TextField('Ссылка на фото', blank=True)
    title = models.CharField('Заголовок', max_length=255)

    def __str__(self):
        return str(self.title)


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    type = models.CharField('Тип', max_length=25, choices=utils.NEWS_TYPE, default=utils.LINK)
    title = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Описание', blank=True)
    link = models.TextField('Ссылка', blank=True)
    datePublication = models.DateTimeField('Дата публикации', auto_now_add=True)
    category = models.ForeignKey(NewsCategory, models.SET_NULL, null=True, blank=True, verbose_name='Категория')

    def __str__(self):
        return str(self.title)


class Publication(models.Model):
    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    title = models.CharField('Заголовок', max_length=255)
    description = models.TextField('Описание', blank=True)
    image = models.TextField('Ссылка на фото', blank=True)
    dateCreated = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return str(self.title)


class UsefulLinks(models.Model):
    class Meta:
        verbose_name = 'Полезная ссылка'
        verbose_name_plural = 'Полезные ссылки'

    title = models.CharField('Заголовок', max_length=255)
    image = models.TextField('Ссылка на фото', blank=True)
    dateCreated = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return str(self.title)


class WorkModel(models.Model):
    unit = models.CharField(max_length=100)
    category = models.IntegerField()
    subCategory = models.IntegerField()
    dateStart = models.DateField(null=True, blank=True)
    dateEnd = models.DateField(null=True, blank=True)
    accepted = models.FloatField()
    name = models.CharField(max_length=255)
    graphCategory = models.FloatField()
    value = models.FloatField()
    color = models.CharField(max_length=100, blank=True)
    year = models.FloatField()
    district = models.FloatField()
    state = models.FloatField()
    isVerified = models.FloatField()

    def __str__(self):
        return self.name