# Generated by Django 4.1 on 2022-08-06 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0003_alter_customuser_address_alter_customuser_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
