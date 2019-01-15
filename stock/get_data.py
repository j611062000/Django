from alpha_vantage.timeseries import TimeSeries
from bs4 import BeautifulSoup as bs
from datetime import datetime
from django.utils import timezone

import requests
import time


def parse_time(datetime_str, datetime_format="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(datetime_str, datetime_format)


class top_20_stocks():

    def __init__(self, last_refreshed=None, date=timezone.now()):
        self.date = date
        self.top_20_list = self.get_top_20_list()
        self.top_20_detail = self.get_top_20_detail(self.top_20_list)

    def get_top_20_list(self):
        url = "https://www.tradingview.com/markets/stocks-usa/market-movers-active/"
        html = requests.get(url)
        soup = bs(html.content, "lxml")

        def filting(x): return x.split(':')[1]

        class_of_ticker = "tv-data-table__row tv-data-table__stroke tv-screener-table__result-row"
        class_of_fullname = "tv-screener__description"
        ticker_name_raw = soup.find_all("tr", class_=class_of_ticker)
        full_name = [x.text[10:]
                     for x in soup.find_all(class_=class_of_fullname)]
        ticker_name = [filting(element['data-symbol'])
                       for element in ticker_name_raw]
        temp = dict()
        for i in range(20):
            temp[ticker_name[i]] = full_name[i]
        return temp

    def get_top_20_detail(self, top_20_list):
        temp = []
        for ticker in top_20_list:
            try:
                time.sleep(10)
                print("Retrieving the data of {}...".format(ticker))
                temp.append(stock_detail(top_20_list[ticker], ticker))
            except:
                pass
        return temp


class stock_detail():

    def __init__(self, name, ticker):
        self.name = name
        self.ticker = ticker
        self.interval_price = self.get_interval_price()
        self.closing_price = self.interval_price[max(self.interval_price)]

    def get_interval_price(self,  token="8BHO3DV69A6T0OPC"):
        ts = TimeSeries(key=token)
        data, meta_data = ts.get_intraday(self.ticker)
        temp = {}
        for interval in data:
            temp[parse_time(interval)] = data[interval]['4. close']
        return temp

# temp = top_20_stocks()
# print(temp.date)
# print(temp.top_20_list)
# print([x.closing_price for x in temp.top_20_detail])
