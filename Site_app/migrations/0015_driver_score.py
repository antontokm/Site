# Generated by Django 4.0 on 2022-01-30 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_app', '0014_remove_driver_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
