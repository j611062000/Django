from django.views.generic.dates import TodayArchiveView
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import generic
from django.urls import reverse
from datetime import datetime

from .get_news import get_news, get_headlines
from .get_data import top_20_stocks, stock_detail
from .models import Trading_Date, Stock_Info, fifteen_mins_interval

import requests


def refresh_data():
    data = top_20_stocks()
    new_top_20_list = Trading_Date.objects.create(
        trading_date=data.date,
        last_refreshed=datetime.now()
    )

    for stock in data.top_20_detail:
        stock_info = Stock_Info.objects.create(
            trading_date=new_top_20_list,
            stock_name=stock.name,
            stock_ticker=stock.ticker,
            closing_price_of_the_day=stock.closing_price
        )

        for interval in stock.interval_price:
            fifteen_mins_interval.objects.create(
                stock=stock_info,
                end_of_interval=interval,
                price_of_the_interval=stock.interval_price[interval]
            )


class StockTodayArchiveView(TodayArchiveView):

    queryset = Trading_Date.objects.all()
    date_field = "trading_date"
    allow_future = True


def stock_detail(request, ticker):
    day = Trading_Date.objects.all().last().stock_info_set.all().get(stock_ticker=ticker)
    stock_interval_price = day.fifteen_mins_interval_set.all().order_by(
        '-end_of_interval')

    return render(
        request,
        'stock/interval_price_for_individual_stock.html',
        {
            'stock_interval_price': stock_interval_price,
            "stock_ticker": ticker,
        }
    )


def checkData(request):
    today = datetime.today().date()
    try:
        most_recent_data_date = Trading_Date.objects.all().last().last_refreshed.date()
        if today > most_recent_data_date:
            refresh_data()
    except:
        refresh_data()
    return redirect(reverse("stock:top_20"))


def stock_welcome(request):
    return render(request, 'stock/stock_home_page.html')

def individual_stock_news(request, ticker):
    stock_full_name=Stock_Info.objects.filter(stock_ticker=ticker)[0].stock_name
    news=get_news(stock_full_name)

    return render(
        request,
        'stock/news_individual_stock.html',
        {
            "news": news,
            "ticker":ticker,
            "stock_full_name":stock_full_name,
        }
    )
def headlines(request):
    news=get_headlines()
    return render(
        request,
        'stock/top_news.html',
        {
            "news": news,
        }
    )