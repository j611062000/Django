# Generated by Django 2.1.4 on 2018-12-14 04:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trading_date',
            name='last_refreshed',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last_refreshed'),
        ),
    ]
