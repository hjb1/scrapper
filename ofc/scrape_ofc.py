import re
import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer
from lxml import html
from collections import namedtuple
from itertools import izip
import time
import sys

root_url = 'http://www.expocadweb.com/17OFC/ec/forms/attendee/vbooth5.aspx?id='



def get_exhibitors(soup):
    try:
        exhibitor_name = soup.find('span', id='lblName').text.encode('utf-8').strip()
    except AttributeError:
        exhibitor_name = ''
    try:
        exhibitor_booth = soup.find('a', id='boothsLink').text.encode('utf-8').strip()
    except AttributeError:
        exhibitor_booth = ''
    try:
        exhibitor_address = soup.find('span', id='lblvbBCardAddr1').text.encode('utf-8').strip()
    except AttributeError:
        exhibitor_address = ''
    try:
        exhibitor_city = soup.find('span', id='lblvbBCardCityStateZip').text.encode('utf-8').strip()
    except AttributeError:
        exhibitor_city = ''
    try:
        exhibitor_country = soup.find('span', id='lblvbBCardCountry').text.encode('utf-8').strip()
    except AttributeError:
        exhibitor_country = ''

    return exhibitor_name, exhibitor_booth, exhibitor_address, exhibitor_city, exhibitor_country, exhibitor_country

def write_csv(exhibitors):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    outfile = 'list.csv'
    with open(outfile, 'a+b') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(exhibitors)


def get_error(soup):
    error = soup.find('span', id = 'lblError')
    if error:
        return True
    else:
        return False

exhibitor_all = []

for i in range(2000):
    response = requests.get(root_url + str(i))

    soup = BeautifulSoup(response.text, 'lxml')

    if get_error(soup) == True:
        #print('booth not found; page: ', i, ' | ', response.url)
        percent = int(round(i/float(2000)*100))
        bar = int(round(percent/5))
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[%-20s] %d%%; %d" % ('='*bar, percent, i))
        sys.stdout.flush()
        continue


    exhibitors = list(get_exhibitors(soup))

    percent = int(round(i/float(2000)*100))
    bar = int(round(percent/5))
    sys.stdout.write('\r')
    # the exact output you're looking for:
    sys.stdout.write("[%-20s] %d%%; %d" % ('='*bar, percent, i))
    sys.stdout.flush()

    #print('Page: ', i, 'List Length: ', len(exhibitors), response.url)

    write_csv(exhibitors)
