import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# Using newegg as an example
myUrl = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards'

# grabs the page
uClient = uReq(myUrl)

page_html = uClient.read()

# closes the client
uClient.close()

#html parsing
page_soup = soup(page_html, 'html.parser')

page_soup.findAll('div', {'class' : 'item-container'})

