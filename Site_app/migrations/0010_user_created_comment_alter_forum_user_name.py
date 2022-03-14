# Generated by Django 4.0 on 2022-01-20 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site_app', '0009_alter_forum_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_created_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='forum',
            name='user_name',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Site_app.user_created_comment'),
        ),
    ]