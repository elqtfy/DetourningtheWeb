import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/27652543/how-to-use-python-requests-to-fake-a-browser-visit"#only possible when the javascript is not requesting to load new stuff. meaning the url should show the whole contecnts of the page.
response = requests.get(url) #returns object
html = response.text
soup = BeautifulSoup(html, "html.parser") #objects!! 
# links = soup.select('a')

# for link in links:
# 	print link.string
# 	print link.get('href')

titles = soup.select('.comment-copy')
for title in titles:
	print title.text.strip().encode('utf-8')
#print html
#which is the exactly same func with curl