import requests
import subprocess
from bs4 import BeautifulSoup
import os
import sys

def download_file(url, local_filename=None):
	if local_filename is None:
		local_filename = url.split('/')[-1]

	if os.path.exists(local_filename):
		return	local_filename

	if not url.startswith('http'):
		url = 'http:'+url

	r = requests.get(url,stream=True)
	with open(local_filename,'wb') as f:
		for chunk in r.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
	return local_filename

def get_images(url):
	html = requests.get(url).text
	soup = BeautifulSoup(html, 'html.parser')
	images = soup.select('img')
	for i, image in enumerate(images):
		img_url = image.get('src')
		savedname = 'frames/'+str(i)+'.jpg'

		try:
			filename = download_file(img_url,savedname)
		except Exception as e:
			print e
			continue
		subprocess.call(['convert','frames/*.jpg','coolgif.gif'])

get_images(sys.argv[1])