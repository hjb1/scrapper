import re
import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer
from lxml import html
from collections import namedtuple
from itertools import izip

comp_num = ''
booth = ''
out = 'heli list.csv'
infile = 'booths.csv'

root_url = ("https://www.rotor.org/fox/vfpcgi.exe?IDCFile=SHOWXHIB.IDC&comp_num={0}&booth={1}&year=2016&user_id=0".format(comp_num, booth))

#'https://www.rotor.org/fox/vfpcgi.exe?IDCFile=SHOWXHIB.IDC&comp_num=&booth=4312&year=2016&user_id=0'

comp_num = ''
booth = ''



def get_exhibitors():
    print 'Parsing Data...'
    global soup #pull variable from global
    global booth
    exhibitors_all = []
    #find where interesting text is
    booth_text = soup.body.div.next_sibling.next_sibling

    #get the name from tags.
    exhibitor_names = booth_text.b.get_text()

    #split the booth text into an iterable list to pull out the address.
    booth_text = booth_text.get_text()
    booths_list = [y for y in (x.strip() for x in booth_text.splitlines()) if y]
    exhibitor_address = booths_list[2] #got the address.

    exhibitor_booths = booth

    exhibitors_all = [exhibitor_names, exhibitor_booths, exhibitor_address]
    return exhibitors_all



def write_csv():
    print 'Writing CSV....'
    with open(out, 'a+b') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(exhibitors_all)


print '\nopening seed file'

with open(infile) as v:
    csv_v = csv.reader(v)
    itercsv = iter(csv_v)
    next(itercsv)
    for line in itercsv:
        booth = line[1]
        comp_num = line[2]
        root_url = ("https://www.rotor.org/fox/vfpcgi.exe?IDCFile=SHOWXHIB.IDC&comp_num={0}&booth={1}&year=2016&user_id=0".format(comp_num, booth))

        response = requests.get(root_url)

        soup = BeautifulSoup(response.text.encode('ascii', 'ignore'), 'lxml')
        exhibitors_all = get_exhibitors()
        print exhibitors_all

        write_csv()

"""
for i in range(800):
    response = requests.get(root_url + str(i))

    soup = BeautifulSoup(response.text, 'lxml', parse_only=SoupStrainer('div'))
    exhibitors_all = map(list, zip(*get_exhibitors()))
    print('Page: ', i, 'List Length: ', len(exhibitors_all), response.url)

    write_csv()
"""
