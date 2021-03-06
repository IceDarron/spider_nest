Scrapy简单介绍

> Scrapy是一个为了爬取网站数据，提取结构性数据而编写的应用框架。 其可以应用在数据挖掘，信息处理或存储历史数据等一系列的程序中。
其最初是为了页面抓取 (更确切来说, 网络抓取 )所设计的， 也可以应用在获取API所返回的数据(例如 Amazon Associates Web Services ) 或者通用的网络爬虫。Scrapy用途广泛，可以用于数据挖掘、监测和自动化测试。

> Scrapy 使用了 Twisted异步网络库来处理网络通讯。整体架构大致如下:

![Image text](https://github.com/IceDarron/spider_nest/blob/master/scrapy_framework.png)

Scrapy主要组件
===
+ 引擎(Scrapy)
用来处理整个系统的数据流处理, 触发事务(框架核心)
+ 调度器(Scheduler)
用来接受引擎发过来的请求, 压入队列中, 并在引擎再次请求的时候返回. 可以想像成一个URL（抓取网页的网址或者说是链接）的优先队列, 由它来决定下一个要抓取的网址是什么, 同时去除重复的网址
+ 下载器(Downloader)
用于下载网页内容, 并将网页内容返回给蜘蛛(Scrapy下载器是建立在twisted这个高效的异步模型上的)
+ 爬虫(Spiders)
爬虫是主要干活的, 用于从特定的网页中提取自己需要的信息, 即所谓的实体(Item)。用户也可以从中提取出链接,让Scrapy继续抓取下一个页面
+ 项目管道(Pipeline)
负责处理爬虫从网页中抽取的实体，主要的功能是持久化实体、验证实体的有效性、清除不需要的信息。当页面被爬虫解析后，将被发送到项目管道，并经过几个特定的次序处理数据。
+ 下载器中间件(Downloader Middlewares)
位于Scrapy引擎和下载器之间的框架，主要是处理Scrapy引擎与下载器之间的请求及响应。
+ 爬虫中间件(Spider Middlewares)
介于Scrapy引擎和爬虫之间的框架，主要工作是处理蜘蛛的响应输入和请求输出。
+ 调度中间件(Scheduler Middewares)
介于Scrapy引擎和调度之间的中间件，从Scrapy引擎发送到调度的请求和响应。

Scrapy运行流程
===
+ 引擎从调度器中取出一个链接(URL)用于接下来的抓取
+ 引擎把URL封装成一个请求(Request)传给下载器
+ 下载器把资源下载下来，并封装成应答包(Response)
+ 爬虫解析Response
+ 解析出实体（Item）,则交给实体管道进行进一步的处理
+ 解析出的是链接（URL）,则把URL交给调度器等待抓取

实践
===
### 安装
```
pip install Scrapy
```

### 创建项目:
```
scrapy startproject your_project_name
```

### 自动创建目录：
```
project_name/
   scrapy.cfg
   project_name/
       __init__.py
       items.py
       pipelines.py
       settings.py
       spiders/
           __init__.
```
+ scrapy.cfg   项目的配置信息，主要为Scrapy命令行工具提供一个基础的配置信息。（真正爬虫相关的配置信息在settings.py文件中）
+ items.py     设置数据存储模板，用于结构化数据，如：Django的Model
+ pipelines    数据处理行为，如：一般结构化的数据持久化
+ settings.py  配置文件，如：递归的层数、并发数，延迟下载等
+ spiders      爬虫目录，如：创建文件，编写爬虫规则

### 运行
```
scrapy crawl spider_name --nolog
```

### 运行scrapy是报import win32api ImportError DLL load 错误
需要安装pywin32 
```
pip install pywin32
```
之后将..\Python\Python35\Lib\site-packages\pywin32_system32里面的所有的文件复制到：C:\Windows\System32
再执行scrapy bench即可。


### 常见问题
```
# Obey robots.txt rules
# because so maney website dont support robot-protocol, it have to be closed. 
  so it shuold be 'ROBOTSTXT_OBEY = False'
ROBOTSTXT_OBEY = False
```

验证码获取时的样式选择器选取错误

重写所有继承的抽象方法-parse

修改header文件中的浏览器版本



