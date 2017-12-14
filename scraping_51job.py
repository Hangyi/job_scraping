from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def get_content(url):
    """获取网页源码"""
    a = urlopen(url)
    html = a.read().decode('gbk')
    return html

def get_bsObj(html):
    """获取bsObj对象"""
    bsObj = BeautifulSoup(html. "lxml")
    return bsObj

def get_position(html):
    reg = re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',re.S)
    items = re.findall(reg, html)
    for i in items:
        print(i[0]+'\t'+i[1]+'\t'+i[2]+'\t'+i[3]+'\t'+i[4]+'\n')

# 这里操作的是bsObj对象
def get_num_position(bsObj):
    """获取一共有多少职位"""
    num_positon = bsObj.find("div", {"class":"rt"})
    return(num_positon.get_text().strip())

# 一共有多少页
# 用bsObj
# num_page = bsObj.find_all(text=re.compile("共\d*页"))
# print(num_page) # 输出是['共39页，到第']

def get_num_page(html):
    """用正则获取有多少页结果"""
    reg = re.compile(r'<span class="td">共(.*?)页(.*?)</span>', re.S)
    items = re.findall(reg, html)
    num_page = items[0][0]
    return(num_page)

url = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=080200&keyword=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95"
html = get_content(url)
num_page = get_num_page(html)
for page in int(num_page):
    print("正在爬取" + str(page) + "页数据...")
    get_
