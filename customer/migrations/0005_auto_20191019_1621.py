# Generated by Django 2.2.4 on 2019-10-19 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
        ('customer', '0004_newslettersession'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.ArticlesModel'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.PostModel'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
