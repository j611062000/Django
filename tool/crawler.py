import requests
import json
from bs4 import BeautifulSoup as bs

# chcp 65001


class raw_data_from_TWSE():

    def __init__(self, date):
        self.date = date
        self.url = "http://www.tse.com.tw/exchangeReport/MI_INDEX20?response=json&date=" + self.date
        html = requests.get(self.url)
        soup = bs(html.content, "lxml")
        self.raw_data = json.loads(soup.get_text())


def data_for_django(date):

    dic = raw_data_from_TWSE(date).raw_data

    temp = []
    for element in dic["data"]:
        # ticker, name, price
        temp.append([element[1], element[2], int(float(element[8]))])

    return (dic["date"], temp)
print(data_for_django("20180905"))
