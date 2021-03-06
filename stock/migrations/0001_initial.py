# Generated by Django 2.1.4 on 2018-12-09 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fifteen_mins_interval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_of_interval', models.DateTimeField(verbose_name='end_of_interval')),
                ('price_of_the_interval', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Stock_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=20)),
                ('stock_ticker', models.CharField(max_length=10)),
                ('closing_price_of_the_day', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Trading_Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trading_date', models.DateTimeField(verbose_name='trading date')),
            ],
        ),
        migrations.AddField(
            model_name='stock_info',
            name='trading_date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Trading_Date'),
        ),
        migrations.AddField(
            model_name='fifteen_mins_interval',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Stock_Info'),
        ),
    ]
