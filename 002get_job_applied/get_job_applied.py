from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import xlwt


url = "http://i.51job.com/userset/my_apply.php?lang=c&type=sh&page=1"
html = urlopen(url)

# a = urlopen(url)
# html = a.read().decode('gbk')
bsObj = BeautifulSoup(html.read(), "lxml")

title = bsObj
# title = bsObj.find("head", {"class": "title"})
print(title)
reg = re.compile('')
items = bsObj.findAll("div",{"class" :"li l1"})
for item in items:
    print(item)
