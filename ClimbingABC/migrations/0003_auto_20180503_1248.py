# Generated by Django 2.0.3 on 2018-05-03 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClimbingABC', '0002_auto_20180503_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='picture',
            field=models.ImageField(default=1, upload_to='category_images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default=1, upload_to='images'),
            preserve_default=False,
        ),
    ]
