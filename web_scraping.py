from urllib import request

from bs4 import BeautifulSoup

import json

import csv

page_url ='https://alansimpson.me/python/scrape_sample.html'

rawpage = request.urlopen(page_url)

soup = BeautifulSoup(rawpage,'html5lib')

content = soup.article

links_list = []

for link in content.find_all('a'):
    try:
        url = link.get('href')
        img = link.img.get ('src')
        text = link.span.text
        links_list.append({'url':url, 'img':img, 'text':text})
    except AttributeError:
        pass


with open('links.json', 'w', encoding='utf-8') as links_file:
    json.dump(links_list, links_file, ensure_ascii=False)


with open('links_CSV.csv', 'w', newline='') as csvout:
    csv_writer = csv.writer(csvout)
    csv_writer.writerow(['url','img','text'])

    for row in links_list:
        csv_writer.writerow([str(row['url']),str(row['img']),str(row['text'])])

print("Done!")
    
