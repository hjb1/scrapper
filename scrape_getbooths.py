from lxml import etree
from StringIO import StringIO
import csv


out = 'booths.csv'
out_data = []

parser = etree.XMLParser(recover=True, remove_blank_text=True)

infile = 'heli.xml'

root = etree.parse(infile, parser)

tag_list = [ "name", "boothnum", "comp_num",]

out_data.append(tag_list[:])

def get_info(booth):
	info = []
	for tag in tag_list:
		node = booth.find(tag)
		if node is not None and node.text:
			info.append(node.text.encode("utf-8"))
	return info

print "\nreading xml..."

booths = root.findall(".//booth")
for booth in booths:
	booth_info = get_info(booth)
	if booth_info:
		out_data.append(booth_info)

print "\nfinished XML, writing file..."

out_file = open (out, "wb")
csv_writer = csv.writer(out_file)
for row in out_data:
	csv_writer.writerow(row)

out_file.close()

print "wrote %s" % out


"""
xmlDoc = open('heli.xml', 'r')
xmlDocData = xmlDoc.read()
xmlDoc.close()
xmlDocTree = etree.parse(StringIO(xmlDocData))

print xmlDocTree.docinfo.doctype

context = etree.iterparse(StringIO(xmlDocData))

booth_dict = {}
booths = []
names = []

for action,elem in context:
	text = elem.text
	if elem.tag == "boothnum":
		booths.append(text)

	if elem.tag == "name":
		names.append(text)

f = open('booths.txt', 'wb')

for item in booths:
	f.write("%s\n" % item)
"""
