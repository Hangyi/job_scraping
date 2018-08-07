import requests
my_headers = {
'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding' : 'gzip',
'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'}

def processing_cookies(my_cookies):
    cookies = {}
    for cookie in my_cookies.split(';'):
        name, value = cookie.strip().split('=',1)
        cookies[name]= value
    return cookies

def steamcn_checkin():
    stcn_cookies =  "此处填cookies"
    cookies = processing_cookies(stcn_cookies)
    r = requests.get('https://steamcn.com/forum.php', cookies=cookies, headers=my_headers)


def readfree_checkin():
    readfree_cookies = "此处填cookies"
    r = requests.get("http://readfree.me/accounts/checkin/", cookies=cookies, headers=my_headers)
    if r.status_code == 200:
        print("readfree签到成功")
    else:
        print("readfree签到不成功")


steamcn_checkin()
readfree_checkin()


