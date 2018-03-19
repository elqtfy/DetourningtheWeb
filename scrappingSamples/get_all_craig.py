import requests
from bs4 import BeautifulSoup
import time

def get_page(s):
	url = "https://newyork.craigslist.org/d/wanted/search/waa"
	#only possible when the javascript is not requesting to load new stuff. 
	#meaning the url should show the whole contecnts of the page.
	response = requests.get(url, params={'s': s}) #returns object
	html = response.text
	soup = BeautifulSoup(html) #objects!! 
	titles = soup.select('.result-title')

	output = []
	for title in titles:
		output.append(title.string.strip().encode('utf-8'))
	return output



start = 0
while start < 2500:
	results = get_page(start)
	for r in results:
		print r

	time.sleep(0.1)
	start = start + 120