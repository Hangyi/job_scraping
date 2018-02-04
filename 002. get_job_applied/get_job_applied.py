import re
import xlwt
import requests

def get_num_page(html):
    """用正则获取有多少页结果"""
    reg = re.compile(r'<span class="td">共(.*?)页，到第</span>', re.S)
    items = re.findall(reg, html)
    num_page = items[0]
    print("一共有" + num_page + "页")
    return(int(num_page))

# 将结果输出到excel
def excel_write(items,index):
    """爬取到的内容写入excel表格"""
    style = xlwt.easyxf('font: name 微软雅黑')
    for item in items: # 职位信息
        print(item)
        for i in range(0,4):
            ws.write(index,i,item[i], style) # 行，列，数据
        index += 1

def log_in():
    """使用cookie绕过登陆"""
    s = requests.Session()
    r = s.get('http://i.51job.com/userset/my_apply.php?lang=c', cookies={这里加上cookie}) # cookie用键值对的格式
    r.encoding='gbk'
    return r.text

def get_current_info(page_number):
    """获取当前页面的信息"""
    url = "http://i.51job.com/userset/my_apply.php?lang=c&type=sh&page=" + str(page_number)
    print(url)
    s = requests.get(url, cookies = {这里加上cookie})
    s.encoding='gbk' # 将编码转化为gbk格式
    page = s.text # 获取文本
    reg = re.compile(r'class="li l1">.*? target="_blank" title="(.*?)".*?<span class="xz" title="(.*?)".*? title="(.*?)".*? <span class="dq" title="(.*?)".*?</span>',re.S)
    items = re.findall(reg, page)
    print(items)
    for i in items:
        print(i)
    return items

html = log_in()
num_page = get_num_page(html)

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet', cell_overwrite_ok=True) # cell_overwrite_ok=True 防止冲突
headData = ['职位', '薪资', '公司', '地区', '日期'] # 表头信息
for column in range(0, 5):
    ws.write(0, column, headData[column], xlwt.easyxf('font: name 微软雅黑, bold on')) # 行，列
 
for i in range(1, num_page+1):
    print("正在爬取" + str(i) + "页数据...")
    index = (i - 1) * 15 + 1
    excel_write(get_current_info(i), index)
wb.save('job_applied_list.xls')


