from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import xlwt

def get_content(page):
    """获取网页源码"""
    url = "http://search.51job.com/list/080200,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595,2," + page + ".html?"
    a = urlopen(url)
    html = a.read().decode('gbk')
    return html

def get_bsObj(html):
    """获取bsObj对象"""
    bsObj = BeautifulSoup(html, "lxml")
    return bsObj

def get_position(html):
    reg = re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',re.S)
    items = re.findall(reg, html)
    # for i in items:
    #     print(i[0]+'\t'+i[1]+'\t'+i[2]+'\t'+i[3]+'\t'+i[4]+'\n')
    return items

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

# 将结果输出到excel
def excel_write(items,index):
    # 爬取到的内容写入excel表格
    for item in items: # 职位信息
        for i in range(0,5):
            # print item[i]
            ws.write(index,i,item[i], xlwt.easyxf('font: name 微软雅黑')) # 行，列，数据
        # print(index)
        index+=1


# url = "http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=080200&keyword=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95"
html = get_content("1")
num_page = int(get_num_page(html))
for page in range(1, num_page):
    print("正在爬取" + str(page) + "页数据...")
    content = get_content(str(page))
    get_position(content)

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
headData = ['招聘职位', '公司', '地址', '薪资', '日期'] # 表头信息
for column in range(0, 5):
    ws.write(0, column, headData[column], xlwt.easyxf('font: name 微软雅黑, bold on')) # 行，列

for i in range(1, num_page):
    index = (i - 1) * 50 + 1
    excel_write(get_position(get_content(str(i))), index)
wb.save('result1.xls')
