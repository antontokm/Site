# Generated by Django 4.0 on 2022-01-23 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_app', '0011_alter_forum_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='user_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
