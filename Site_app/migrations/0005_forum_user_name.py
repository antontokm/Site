# Generated by Django 4.0 on 2022-01-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_app', '0004_forum'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='user_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]