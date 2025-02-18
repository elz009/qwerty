# Generated by Django 4.0.10 on 2024-07-31 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_indicator_color_indicator_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=255)),
                ('category', models.IntegerField()),
                ('subCategory', models.IntegerField()),
                ('dateStart', models.DateField(blank=True, null=True)),
                ('dateEnd', models.DateField(blank=True, null=True)),
                ('accepted', models.FloatField()),
                ('name', models.CharField(max_length=255)),
                ('graphCategory', models.FloatField()),
                ('value', models.FloatField()),
                ('color', models.CharField(blank=True, max_length=255)),
                ('year', models.IntegerField()),
                ('district', models.FloatField()),
                ('state', models.FloatField()),
                ('isVerified', models.FloatField()),
            ],
        ),
    ]
