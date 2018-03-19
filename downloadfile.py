import requests

from PIL import Image, ImageFilter, ImageDraw, ImageFont

# response = requests.get('https://www.parents.com/search/site/crying-baby/')

# with open('baby.jpg','wb') as outfile:
# 	outfile.write(response.content)

# def write_text(imgfilename,text):
	# im = Image.open(imgfilename)
	# canvas = ImageDraw.Draw(im)
	# canvas.rectangle([0,125, im.size[0],170],fill=(0,0,0))
	# im.save(imgfilename + '.modified.jpg')
	# fnt = ImageFont.truetype('/Library/Fonts/BrushScriptStd.otf',40)
	# canvas.text((10,125), text, font=fnt, fill=(255,255,255))

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


def get_shutterstock_imgaes(q):
	url = 'https://www.shuttertock.com/search'
	params = {'searchterm':q}
	html = requests.got(url,params=params).text
	soup = BeutifulSoup(html,'html.parser')
	images = soup.select('.img-wrap img')

	for image in images:
		img_url = 'https:'+image.get('src')
		print img_url
		download_file(img_url)

def get_images(url):
	html = requests.get(url).text
	soup = BeutifulSoup(html, 'html.parser')
	images = soup.select('img')
	for image in images:
		img_url = image.get('src')
		try:
			download_file(img_url)
		except:
			continue

get_images('https://unsplash.com/search/photos/random')
#get_images('https://www.bing.com/image/search?q=babies+crying&FORM=HDRSC2')
#get_images('baby crying')
