from django.db import models
from django.utils import timezone
from . import get_data


class Trading_Date(models.Model):
    trading_date = models.DateTimeField('trading date')
    last_refreshed = models.DateTimeField('last_refreshed', default = timezone.now)


    def __str__(self):
        return str("Trading_Date:{}, last_refreshed: {}".format(self.trading_date,self.last_refreshed))
    # def was_published_recently(self):
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Stock_Info(models.Model):
    stock_name = models.CharField(max_length=20)
    stock_ticker = models.CharField(max_length=10)
    closing_price_of_the_day = models.CharField(max_length=10)
    trading_date = models.ForeignKey(Trading_Date, on_delete=models.CASCADE)


    def __str__(self):
        return "Date: {}, Ticker:{}, Closing price: {}".format(self.trading_date, self.stock_ticker,self.closing_price_of_the_day)


class fifteen_mins_interval(models.Model):
    stock = models.ForeignKey(Stock_Info, on_delete = models.CASCADE)
    end_of_interval = models.DateTimeField('end_of_interval')
    price_of_the_interval = models.FloatField(default=0)

    def __str__(self):
        return "Stock:{}".format(self.stock)
