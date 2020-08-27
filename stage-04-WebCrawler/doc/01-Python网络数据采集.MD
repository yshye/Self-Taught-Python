## 网络爬虫初识

[<< 返回目录](../README.MD)

### 1. 概念
> 网络爬虫（又称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。
>
>- 来自《百度百科》

### 2. Python3 实现简单的爬虫
#### 2.1 使用 `urllib.request` 
> urllib 为Python内置库，直接引用即可
```python
from urllib.request import urlopen

def test1():
    html = urlopen("https://www.baidu.com")
    print(html.read())
```

#### 2.2 使用`requests`库
> requests 是第三方库，需要安装才可以使用。 [https://github.com/requests/requests](https://github.com/requests/requests)

1. 安装
> pip install requests

2. 示例
```python
import requests
 
if __name__ == '__main__':
    target = "http://fanyi.baidu.com/"
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    print(req.text)
```

### 2. BeautifulSoup

#### 2.1 安装
```shell script
pip install beautifulsoup4
```

#### 2.2 初次使用
```shell script

from urllib.request import urlopen
from bs4 import BeautifulSoup

def test2():
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
    # features = html.parser:Python标准库；=lxml:lxml HTML 解析器；= ["lxml-xml"]/"xml" lxml XML 解析器; =html5lib:html5lib解析
    html_bs = BeautifulSoup(html.read(), features="lxml")
    # 建议使用 lxml的解析，因为效率更高. 在Python2.7.3之前的版本和Python3中3.2.2之前的版本,必须安装lxml或html5lib, 因为那些Python版本的标准库中内置的HTML解析方法不够稳定.
    print(html_bs.h1)
    print(html_bs.html.body.h1)
    print(html_bs.html.h1)
    print(html_bs.body.h1)
```