import re
import csv
import requests
import bs4

root_url = 'https://n2a.goexposoftware.com'
index_url = root_url + '/events/ss17/goExpo/exhibitor/listExhibitorProfiles.php?keyword=&search_field_X=display_name&search_field_Y=&category=&state_prov=CA&state_prov_new=&search=Search&new='

links = []

response = requests.get(index_url)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

for table_row in soup.findAll(".ffTableSet tr"):
	table_cells = table_row.findAll('td')

	if len(table_cells) > 0:
		relative_link_details = table_cells.find('a')['href']
		absolute_link_details = url_to_scrape + relative_link_to_inmate_details
		links.append(relative_link_details)
        print(relative_link_details)
