from django.test import TestCase
from models import Trading_Date, Stock_Info
from django.utils import timezone
from stock.get_data import top_20_stocks, stock_detail


def refresh_data():
    new_top_20_list = Trading_Date.objects.create


class dataGetTest(TestCase):

    def setUp(self):
        data = top_20_stocks()
        Trading_Date.objects.create(trading_date=data.date)
        self.assertEqual(data.top_20_detail, 20)
        for stock in data.top_20_detail:
            Stock_Info.objects.create(trading_date=new_top_20_list, stock_name=stock.name,
                                  stock_ticker=stock.ticker, closing_price_of_the_day=stock.closing_price)

    # def test_if_data_collect_correct(self):
    #     """Animals that can speak are correctly identified"""
    #     lion = Animal.objects.get(name="lion")
    #     cat = Animal.objects.get(name="cat")
    #     self.assertEqual(lion.speak(), 'The lion says "roar"')
    #     self.assertEqual(cat.speak(), 'The cat says "meow"')
