from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import json
#40 80 100 120 140....
driver = webdriver.Chrome()
tweets_tone_text = ""
tweets = []
script = '''
window.scrollBy(0, 3000)
'''
def get_scroll(scrollnum, tweets_tone_text): #3times scroll
	for i in range(0, scrollnum):
		#data = json.loads(tweets)
		driver.execute_script(script)
		time.sleep(3)

	items = driver.find_elements_by_css_selector('p.tweet-text')
	#grab whole tweets from 0 to the end of scroll
	j = 0
	for item in items:
		tweet = {
			"text" : item.text  #j : item.text
		}
		# print tweet
		# j += 1
		# tweets.append(tweet)
		tweets_tone_text += item.text
		if j not in tweets:
			print tweet
			j += 1
			tweets.append(tweet)
		# tweet = {
		# 	j : item.text
		# }
		# # print tweet
		# # j += 1
		# # tweets.append(tweet)
		# if str(j) not in tweets:
		# 	print tweet
		# 	j += 1
		# 	tweets.append(tweet)
	return tweets_tone_text
	

url = 'https://twitter.com/search?q=%23sigh&src=typd'
driver.get(url)

tweets_tone = {
	"text" : get_scroll(20, tweets_tone_text)
}

outfile = open('tweets.json', 'w')
json.dump(tweets, outfile, indent=2)
outfile.close()

outfile2 = open('tone_tweets.json', 'w')
json.dump(tweets_tone, outfile2, indent=4)
outfile2.close()


driver.quit()