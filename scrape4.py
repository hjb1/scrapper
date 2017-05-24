import re
import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer
from lxml import html

root_url = 'https://n2a.goexposoftware.com/events/ss17/goExpo/'
index_url = root_url + 'exhibitor/listExhibitorProfiles.php?keyword=&search_field_X=display_name&search_field_Y=&category=&state_prov=CA&state_prov_new=&search=Search&new='

links = []

def get_page_urls():
    response = requests.get(index_url)
    pattern = re.compile("exhibitor/view")
    soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('a'))
    for a in soup.findAll('a', href=pattern):
            #print(root_url + a['href'])
            links.append(root_url + a['href'])
    return links

print(get_page_urls())

login_url = "https://n2a.goexposoftware.com/events/ss17/goExpo/public/login.php?&t=bg&ign=1&ut=at"

payload = {
    "ext_id": "32076",
    "last_name": "sierveld",
    "ff_form_refresh": "",
    "ff_submit": "Login"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
    'referer': login_url
    }



session_requests = requests.session()
result = session_requests.get(login_url)

result = session_requests.post(
    login_url,
    data = payload,
    headers = headers
)

rows = []

for url in links:
    result = session_requests.get(
        url,
        headers = headers
    )
    soup1 = BeautifulSoup(result.text, 'lxml')
    tables = soup1.find('table', attrs={'cellpadding':'0'})

    print(tables.prettify().encode('UTF-8'))


with open('output_file.csv', 'wb') as f:
    writer = csv.writer(f)
