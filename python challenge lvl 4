import requests
import re
# Divi
url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022" 
r=requests.session()
out=r.get(url)
out=re.search('(?<=and the next nothing is ).*', out.text)
while(out!=None):
  url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+out[0]
  out=r.get(url)
  out=re.search('(?<=and the next nothing is ).*', out.text)

print(url)
