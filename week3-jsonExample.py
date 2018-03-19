import requests

url = '' #something if you seeing something related callback recall, delete it from the url
#example- fox news 'lol' article results
#go to network in console after searching for a thing and see if there's anything look like data
#copy as cUrl
results = requests.get(url)
docs = results['response']['docs']
print results.json()
#print docs
for doc in docs:
	print doc['title']