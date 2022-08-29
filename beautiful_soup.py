import requests
from bs4 import BeautifulSoup

url ='http://www.nytimes.com'
source_code = requests.get(url)
plain_text = source_code.text
soup = BeautifulSoup(plain_text,'html.parser')

for link in soup.findAll('h2',{'class':'css-14bttnj esl82me0'}):
    #href = link.get('href')
    title = link.string
    #print(href)
    print(title)
