import requests

url = "https://newyork.craigslist.org/d/barter/search/bar"
response = requests.get(url) #returns object
print response.text
#html = response.text
#print html
#which is the exactly same func with curl