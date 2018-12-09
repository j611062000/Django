from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
import requests
import json

url = "http://wwwc.twse.com.tw/exchangeReport/MI_INDEX20?response=json&date"
html = requests.get(url)
soup = bs(html.content, "html.parser")
python_data = json.loads(soup.get_text())

def get_data(date=None):
	time = python_data['date']
	temp = {}
	for element in python_data['data']:
		temp[element[1]] = element[2:]
	return (time, temp)

print(get_data()[1])