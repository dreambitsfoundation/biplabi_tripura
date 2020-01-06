# Generated by Django 2.2.4 on 2019-09-08 20:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='head_comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='last_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]