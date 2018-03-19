import requests
from bs4 import BeautifulSoup

url = "https://newyork.craigslist.org/d/wanted/search/waa"#only possible when the javascript is not requesting to load new stuff. meaning the url should show the whole contecnts of the page.
response = requests.get(url) #returns object
html = response.text

soup = BeautifulSoup(html) #objects!! 
# links = soup.select('a')

# for link in links:
# 	print link.string
# 	print link.get('href')

titles = soup.select('.result-title')
for title in titles:
	print title.string.strip().encode('utf-8')
#print html
#which is the exactly same func with curl