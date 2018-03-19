from bs4 import BeautifulSoup
import requests
import urllib
import time

start_url = 'https://www.urbandictionary.com/?page='

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
            print title.text
            print defs.text
            print example.text
            print author.text

        except Exception as e:
            print e
            continue

def get_total_pages(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    totalpages = soup.select('.pagination')
    lenPage=len(totalpages[0].select('a'))
    href = totalpages[0].select('a')[6].get('href')
    href = href.replace('/?page=','')
    return href #totalpages[0].select('a')[6].get('href')

totalpage = int(get_total_pages('https://www.urbandictionary.com'))+1

#print totalpage 

for pagenum in range(1,totalpage):
    #print start_url+str(pagenum)
    get_things_out(start_url+str(pagenum))
    time.sleep(0.2)
