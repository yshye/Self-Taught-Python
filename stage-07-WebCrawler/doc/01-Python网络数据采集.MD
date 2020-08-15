## Python网络数据采集

### 1. 抓取网页数据
```python
from urllib.request import urlopen

def test1():
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    print(html.read())
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