from bs4 import BeautifulSoup
import requests , shutil , datetime ,os
r = requests.get("https://www.nationalgeographic.com/photography/photo-of-the-day/")
data = r.content
# print data
soup = BeautifulSoup(data , "html.parser")
# print soup.prettify()
ImageUrl = ''
for link in soup.find_all('script'):
	if link.get_text().find('aemLeadImage') != -1:
 # print(link)
		ImageUrl = link.get_text()
ImageUrl = ImageUrl[ImageUrl.find('aemLeadImage\': \'')+ 16 : ]
ImageUrl = ImageUrl[: ImageUrl.find('\'') ]
print (ImageUrl)
r = requests.get(ImageUrl , stream=True)
data = r.raw
print (data)
with open("NatGeo" + os.sep + str(datetime.datetime.today().date()) + ".jpg", 'wb') as out_file:
 shutil.copyfileobj(r.raw, out_file)
del r
os.startfile(os.getcwd()+os.sep +"NatGeo" + os.sep + str(datetime.datetime.today().date()) + ".jpg")
input('kk')