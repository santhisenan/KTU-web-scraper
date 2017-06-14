import urllib2
from bs4 import BeautifulSoup

page_url = 'https://ktu.edu.in/home.htm'
html_page = urllib2.urlopen(page_url)

soup = BeautifulSoup(html_page, 'html.parser')

box = soup.find('ul', attrs={'class':'annuncement'})

news = box.text.strip()

print news
