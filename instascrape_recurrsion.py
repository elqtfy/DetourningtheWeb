from selenium import webdriver
import os
import requests
import time
import subprocess
import sys
import glob
import fnmatch
import os

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

driver = webdriver.Firefox()
#StaleElementError -> firefox
def insta_gif(tags): 
##scrape instagram with a tag and download all the images with the size of 293x293
	driver.get('https://www.instagram.com/explore/tags/'+tags+'/')
	#driver.get(tags)

	for x in range(0,10):
		driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
		time.sleep(2)

	images = driver.find_elements_by_css_selector('img')

	for i,image in enumerate(images):
		url = image.get_attribute('src')

		savedname = 'mypics/' + str(i)+'.jpg'
		composedname = 'instacompose/' + str(i)+'.jpg' #####subdirectory should be made.

		try:
			filename = download_file(url,savedname)
			subprocess.call(['convert',savedname,'-resize','293x293',savedname]) #RESIZING

		except Exception as e:
			print e
			continue
		##OVERLAY PART
		# if i > 0:	
		# 	presavedname = 'mypics/' + str(i-1)+'.jpg'
		# 	subprocess.call(['composite','-blend','40x60%',presavedname,savedname, presavedname])
	driver.quit()

def composite_images(img1,img2,subfolder):
	newimg = 'mypics/'+str(subfolder)+'/'+'newimg'+'.jpg'
	#newimg = 'mypics/'+'newimg'+'.jpg' 
	subprocess.call(['composite','-blend','40x60%',img1,img2,newimg])
	return newimg


tag = sys.argv[1] 
insta_gif(tag)
images = []
# this is checking the toppest parent directory.
for root, dirnames, filenames in os.walk('mypics'):
    for filename in fnmatch.filter(filenames, '*.jpg'):
        images.append(os.path.join(root, filename))
base_image = images[0]
images = images[1:]
subprocess.call(['mkdir','mypics/'+str(0)])

for img in images:
	new_image  = composite_images(base_image,img,0)

subprocess.call(['convert','mypics/*.jpg','mypics/'+tag+'.gif'])
subprocess.call(['open','mypics/'+tag+'.gif'])
#subprocess.call(['rm','-r','mypics/*.jpg'])

# for img in images:
#   new_image = overlay(base_image, img)
#   base_image = new_image

#######psedo code############
# def overlay(img1, img2):
#     return newimg


# images = glob.glob('source_images/*.jpg'):
# base_image = images[0]
# images = images[1:]

# for img in images:
#   new_image = overlay(base_image, img)
#   base_image = new_image
##############################

