# Generated by Django 4.0.10 on 2024-07-31 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_workmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workmodel',
            name='color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='workmodel',
            name='unit',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workmodel',
            name='year',
            field=models.FloatField(),
        ),
    ]
