from bs4 import BeautifulSoup
import requests
import urllib
import time

start_url = 'http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20'

def get_things_out(url, pagenumber=1):
    html = urllib.urlopen(url+str(pagenumber)).read()
    soup = BeautifulSoup(html, 'html.parser')
    entities = soup.select('.def-panel')
    for entity in entities:
        try:
            title = entity.select('div')[4].a#.get('a')#title
            defs = entity.select('div')[5]#definition
            example = entity.select('div')[6]#example
            author = entity.select('div')[7]
            #vote = entity.select('div')[9]#vote?
            print title.text, defs.text, example.text, author.text

        except Exception as e:
            print e
            continue

# def get_taag(url):
#     html = urllib.urlopen(url).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     taag = soup.select('#taag_output_text')[0]
# 	print taag
html = urllib.urlopen(start_url).read()
soup = BeautifulSoup(html, 'html.parser')
taag = soup.select("#taag_output_text")#.innerHTML#pre#taag_output_text.fig
#for child in taag.children:
#print len(taag)
print taag
#    print child