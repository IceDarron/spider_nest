# encoding:UTF-8
import urllib
import urllib.request


def gethtml(url):
    '''
    :description: 提供简单的页面信息获取
    :param url: 抓取的页面地址
    :return: 返回页面信息
    '''
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def searchInfoByKeyWord_baidu(keyWord):
    '''
    :description: 通过一个关键字返回在百度搜索的结果
    :param keyWord: 搜索关键字
    :return: 返回搜索结果
    '''
    data = {}
    data['word'] = keyWord

    url_values = urllib.parse.urlencode(data)
    url = "http://www.baidu.com/s?"
    full_url = url + url_values

    data = urllib.request.urlopen(full_url).read()
    data = data.decode('UTF-8')
    return data
