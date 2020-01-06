# Generated by Django 2.2.4 on 2019-09-10 21:07

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20190911_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('init_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published', models.BooleanField(default=False)),
                ('posts', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=None)),
                ('articles', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=None)),
            ],
        ),
    ]