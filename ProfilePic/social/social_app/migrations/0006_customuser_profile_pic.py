# Generated by Django 4.1 on 2022-08-07 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0005_remove_customuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
