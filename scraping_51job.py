from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=080200&keyword=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95")
bsObj = BeautifulSoup(html, "lxml")

namelist = bsObj.findAll("span",{"class":"t4"})
for name in namelist:
    print(name.get_text())