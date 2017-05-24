import re
import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer
from lxml import html

root_url = 'https://n2a.goexposoftware.com/events/ss17/goExpo/'
index_url = root_url + 'exhibitor/listExhibitorProfiles.php?keyword=&search_field_X=display_name&search_field_Y=&category=&state_prov=CA&state_prov_new=&search=Search&new='

#pattern = re.compile(r'*exhibitor*')

links = []

def get_page_urls():
    response = session.requests.get(index_url)
    pattern = re.compile("exhibitor/view")
    soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('a'))
    for a in soup.findAll('a', href=pattern):
            print(root_url + a['href'])
            links.append(root_url + a['href'])
    return links



print(get_page_urls())


for td in row.find_all('td'):
    for div in td.find_all('div'):
        company = unicode.strip(div.text)
        print(company)
