# Generated by Django 4.0 on 2022-01-31 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_app', '0018_alter_driver_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]