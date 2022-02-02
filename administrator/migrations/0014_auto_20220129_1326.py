# Generated by Django 3.2.8 on 2022-01-29 07:56

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0013_advideomodel_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adimagemodel',
            name='tall_image_id',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='adimagemodel',
            name='wide_image_id',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='articlesmodel',
            name='photos',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(default=dict), null=True, size=None),
        ),
    ]