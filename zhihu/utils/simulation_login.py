# encoding:UTF-8
import urllib.request
import urllib
import gzip
import http.cookiejar
import os


# 定义一个方法用于生成请求头信息，处理cookie
def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()

    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


# 定义一个方法来解压返回信息
def ungzip(data):
    try:  # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data


# 封装头信息，伪装成浏览器
header_login = {
    'Connection': 'keep-alive'
    , 'Content-Length': '291'
    , 'Cache-Control': 'max-age=0'
    , 'Origin': 'http://kq.neusoft.com'
    , 'Upgrade-Insecure-Requests': '1'
    , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    , 'Content-Type': 'application/x-www-form-urlencoded'
    , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    , 'Referer': 'http://kq.neusoft.com/index.jsp'
    , 'Accept-Encoding': 'gzip, deflate'
    , 'Accept-Language': 'zh-CN,zh;q=0.8'
    , 'Cookie': 'JSESSIONID=8R9NZn9cpDQ2Nv1QtTvCj41wv2v1Kkkt04Pw4WdpwMN3hNRQ7VYl!-1309255234'
}
header_sign = {
    'Connection': 'keep-alive'
    , 'Content-Length': '24'
    , 'Cache-Control': 'max-age=0'
    , 'Origin': 'http://kq.neusoft.com'
    , 'Upgrade-Insecure-Requests': '1'
    , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    , 'Content-Type': 'application/x-www-form-urlencoded'
    , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    , 'Referer': 'http://kq.neusoft.com/attendance.jsp?error=6'
    , 'Accept-Encoding': 'gzip, deflate'
    , 'Accept-Language': 'zh-CN,zh;q=0.8'
    , 'Cookie': 'JSESSIONID=21gcZyRdnpnJ2fGy5nPRyTGSXGKLc1qTvHq1xX4lQQrpyLKD87Gy!-1309255234'
}
header_exit = {
    'Host': 'kq.neusoft.com'
    , 'Connection': 'keep-alive'
    , 'Upgrade-Insecure-Requests': '1'
    , 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    , 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    , 'Referer': 'http://kq.neusoft.com/close.jsp'
    , 'Accept-Encoding': 'gzip, deflate, sdch'
    , 'Accept-Language': 'zh-CN,zh;q=0.8'
    , 'Cookie': 'JSESSIONID=VwRtZyvDb2QX1hn5nk7tf8cTQMxGNyM9Bxc64cGC3y2GGSZMHpgT!-1309255234'
}




# 发送请求
def requestpage(header):
    url = 'http://kq.neusoft.com/login.jsp'
    opener = getOpener(header)

    id = 'rongxn'  # 你的用户名
    password = 'RONGnx@0429'  # 你的密码
    postDict = {
        'email': id
        , 'password': password
    }

    postdata = urllib.parse.urlencode(postDict).encode()
    response = opener.open(url, postdata)
    data = response.read()
    data = ungzip(data)
    return data


def openbrowser(name):
    if name == 'chrome':
        os.startfile("C:\\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe")
    return 0



# 登录
print(requestpage(header_login))
# 打卡
print(requestpage(header_sign))
# 退出
print(requestpage(header_exit))
