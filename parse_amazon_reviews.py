import json
from textblob import Textblob

infile = open('review.json','r')
reviews = json.load(infile)

total_stars = 0
all_adjectives = {} #dictionary item
for review in reviews:
	blob = TextBlob(review['body'])
	for tag in blob.tags:
		if tag[1] == 'JJ': #adjective
			word = tag[0]
			if word	in all_adjectives:
				all_adjectives[word] += 1
			else:
				all_adjectives[word] = 1
			#print tag[0]
	#print review['title']

print all_adjectives
infile.close()