import urllib2
import re
import time

url = raw_input("Enter the url of the webpage with https:// : ")
new = urllib2.urlopen(url)
html= new.read()

jk = re.compile('img src=[ "](.*?)"')
imgurls = re.findall(jk,html)

print imgurls
imgurls=imgurls+['\0']

a=0
iurls = open('iurls.txt','a')

while(1):
	iurls.write(imgurls[a]+"\n")
	a+=1
	if(imgurls[a]=='\0'):
		break

iurls.close()
print "\n\n\t\t\t\t\t\tFile created with the image urls in it\n\t\t\t\t\t\topen iurls.txt"

time.sleep(10)