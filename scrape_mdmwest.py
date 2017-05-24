import re
import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer
from lxml import html
from collections import namedtuple
from itertools import izip

root_url = 'http://mdmwest.mddionline.com/exhibitors?search_api_views_fulltext=&page='



def get_exhibitors():
    exhibitors = namedtuple('exhibitors', ['names', 'booths', 'citys'])
    global soup
    exhibitor_names = [name.text.encode('utf-8').strip() for name in soup.find_all('div', attrs={'class':'views-field views-field-title col-sm-7'})]
    exhibitor_booths = [booth.text.encode('utf-8').strip() for booth in soup.find_all('div', attrs={'class':'views-field views-field-field-booth-number col-sm-2'})]
    exhibitor_city = [city.text.encode('utf-8').strip() for city in soup.find_all('div', attrs={'class':'views-field views-field-field-exhibitor-city'})]

    return exhibitors(exhibitor_names, exhibitor_booths, exhibitor_city)

def write_csv():
    with open('list.csv', 'a+b') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(exhibitors_all)





for i in range(0,1):
    response = requests.get(root_url + str(i))

    soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('div'))
    exhibitors_all = map(list, zip(*get_exhibitors()))
    print('Page: ', i, 'List Length: ', len(exhibitors_all), response.url)

    write_csv()
