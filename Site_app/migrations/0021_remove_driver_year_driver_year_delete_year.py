# Generated by Django 4.0 on 2022-12-11 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_app', '0020_year_driver_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='year',
        ),
        migrations.AddField(
            model_name='driver',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]
