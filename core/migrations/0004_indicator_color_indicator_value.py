# Generated by Django 4.0.10 on 2024-06-02 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_indicator_graphcategory_indicator_name_metadata_icon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='color',
            field=models.CharField(blank=True, max_length=255, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='indicator',
            name='value',
            field=models.FloatField(default=0, verbose_name='Значение'),
        ),
    ]