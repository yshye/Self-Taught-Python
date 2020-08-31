## 网络爬虫初识

[<< 返回目录](../README.MD)

### 1. 概念
> 网络爬虫（又称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常的称为网页追逐者），是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。
>
>- 来自《百度百科》

### 2. 使用 `urllib.request` 
> urllib 为Python内置库，直接引用即可
```python
from urllib.request import urlopen

def test1():
    html = urlopen("https://www.baidu.com")
    print(html.read())
```

### 3 使用`requests`库
> requests 是第三方库，需要安装才可以使用。 [https://github.com/requests/requests](https://github.com/requests/requests)

#### 3.1 安装
> pip install requests

#### 3.2 示例
```python
import requests
 
if __name__ == '__main__':
    target = "http://fanyi.baidu.com/"
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    print(req.text)
```

#### 3.3 request发送模块
##### headers、params
```python
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

# 这是目标url
# url = 'https://www.baidu.com/s?wd=python'

# 最后有没有问号结果都一样
url = 'https://www.baidu.com/s?'

# 请求参数是一个字典 即wd=python
kw = {'wd': 'python'}

# 带上请求参数发起请求，获取响应
response = requests.get(url, headers=headers, params=kw)

print(response.content)
```

##### cookie
```python
import requests

url = 'https://github.com/USER_NAME'

# 1. 请求头中携带cookie
headers = {
    # 从浏览器中复制过来的User-Agent
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
    # 从浏览器中复制过来的Cookie
    'Cookie': 'xxx这里是复制过来的cookie字符串'
}
# resp = requests.get(url, headers=headers)

# 2. 构造cookies字典
cookies_str = '从浏览器中copy过来的cookies字符串'
cookies_dict = {cookie.split('=')[0]:cookie.split('=')[-1] for cookie in cookies_str.split('; ')}
# 请求头参数字典中携带cookie字符串
resp = requests.get(url, headers=headers, cookies=cookies_dict)
# 3. cookieJar对象转换为cookies字典的方法
# 3.1 转换方法
# `cookies_dict = requests.utils.dict_from_cookiejar(response.cookies)`
# 3.2 其中response.cookies返回的就是cookieJar类型的对象
# 3.3 `requests.utils.dict_from_cookiejar`函数返回cookies字典

print(resp.text)
```

##### 超时参数timeout
>在平时网上冲浪的过程中，我们经常会遇到网络波动，这个时候，一个请求等了很久可能任然没有结果。
>
>在爬虫中，一个请求很久没有结果，就会让整个项目的效率变得非常低，这个时候我们就需要对请求进行强制要求，让他必须在特定的时间内返回结果，否则就报错。

1. 超时参数timeout的使用方法

   `response = requests.get(url, timeout=3)`

2. timeout=3表示：发送请求后，3秒钟内返回响应，否则就抛出异常
```python
import requests
url = 'https://twitter.com'
response = requests.get(url, timeout=3)     # 设置超时时间
```

##### proxy代理参数
###### 正向代理和反向代理的区别
1. 从发送请求的一方的角度，来区分正向或反向代理
2. 为浏览器或客户端（发送请求的一方）转发请求的，叫做正向代理
   - 浏览器知道最终处理请求的服务器的真实ip地址，例如VPN
3. 不为浏览器或客户端（发送请求的一方）转发请求、而是为最终处理请求的服务器转发请求的，叫做反向代理
   - 浏览器不知道服务器的真实地址，例如nginx

###### 代理ip（代理服务器）的分类

1. 根据代理ip的匿名程度，代理IP可以分为下面三类：

   - 透明代理(Transparent Proxy)：透明代理虽然可以直接“隐藏”你的IP地址，但是还是可以查到你是谁。目标服务器接收到的请求头如下：

     ```
     REMOTE_ADDR = Proxy IP
     HTTP_VIA = Proxy IP
     HTTP_X_FORWARDED_FOR = Your IP
     ```

   - 匿名代理(Anonymous Proxy)：使用匿名代理，别人只能知道你用了代理，无法知道你是谁。目标服务器接收到的请求头如下：

     ```
     REMOTE_ADDR = proxy IP
     HTTP_VIA = proxy IP
     HTTP_X_FORWARDED_FOR = proxy IP
     ```

   - 高匿代理(Elite proxy或High Anonymity Proxy)：高匿代理让别人根本无法发现你是在用代理，所以是最好的选择。**毫无疑问使用高匿代理效果最好**。目标服务器接收到的请求头如下：

     ```
     REMOTE_ADDR = Proxy IP
     HTTP_VIA = not determined
     HTTP_X_FORWARDED_FOR = not determined
     ```

2. 根据网站所使用的协议不同，需要使用相应协议的代理服务。从代理服务请求使用的协议可以分为：

   - http代理：目标url为http协议
   - https代理：目标url为https协议
   - socks隧道代理（例如socks5代理）等：
     1. socks 代理只是简单地传递数据包，不关心是何种应用协议（FTP、HTTP和HTTPS等）。
     2. socks 代理比http、https代理耗时少。
     3. socks 代理可以转发http和https的请求
###### proxies代理参数的使用

> 为了让服务器以为不是同一个客户端在请求；为了防止频繁向一个域名发送请求被封ip，所以我们需要使用代理ip；那么我们接下来要学习requests模块是如何使用代理ip的

- 用法：

```python
response = requests.get(url, proxies=proxies)
```

- proxies的形式：字典

- 例如：

  ```python
  proxies = { 
      "http": "http://12.34.56.79:9527", 
      "https": "https://12.34.56.79:9527", 
  }
  ```

- 注意：如果proxies字典中包含有多个键值对，发送请求时将按照url地址的协议来选择使用相应的代理ip

##### verify参数忽略CA证书
```python
import requests
url = "https://sam.huat.edu.cn:8443/selfservice/"
response = requests.get(url)
```
> 运行代码将会抛出包含`ssl.CertificateError ...`字样的异常.
>
>为了在代码中能够正常的请求，我们使用`verify=False`参数，此时requests模块发送请求将不做CA证书的验证：verify参数能够忽略CA证书的认证
```python
import requests
url = "https://sam.huat.edu.cn:8443/selfservice/" 
response = requests.get(url,verify=False)
```

**\* 使用verify参数忽略CA证书**

#### 3.4 response响应对象
> 观察上边代码运行结果发现，有好多乱码；这是因为编解码使用的字符集不同早造成的；我们尝试使用下边的办法来解决中文乱码问题

```python
# 1.2.2-response.content
import requests 

# 目标url
url = 'https://www.baidu.com' 

# 向目标url发送get请求
response = requests.get(url)

# 打印响应内容
# print(response.text)
print(response.content.decode()) # 注意这里！
```

1. **response.text**是`requests`模块按照`chardet`模块推测出的编码字符集进行解码的结果
2. 网络传输的字符串都是`bytes`类型的，所以`response.text = response.content.decode('推测出的编码字符集')`
3. 我们可以在网页源码中搜索`charset`，尝试参考该编码字符集，注意存在不准确的情况

##### response.text 和response.content的区别：

 - response.text
   - 类型：str
   - 解码类型： requests模块自动根据HTTP 头部对响应的编码作出有根据的推测，推测的文本编码
 - response.content
   - 类型：bytes
   - 解码类型： 没有指定
   
##### 通过对response.content进行decode，来解决中文乱码

- `response.content.decode()` 默认utf-8
- `response.content.decode("GBK")`
- 常见的编码字符集
  - utf-8
  - gbk
  - gb2312
  - ascii  （读音：阿斯克码）	
  - iso-8859-1

#### 3.5 response响应对象的其它常用属性或方法

> `response = requests.get(url)`中response是发送请求获取的响应对象；response响应对象中除了text、content获取响应内容以外还有其它常用的属性或方法：

- `response.url`响应的url；有时候响应的url和请求的url并不一致
- `response.status_code` 响应状态码
- `response.request.headers` 响应对应的请求头
- `response.headers` 响应头
- `response.request._cookies` 响应对应请求的cookie；返回cookieJar类型
- `response.cookies` 响应的cookie（经过了set-cookie动作；返回cookieJar类型
- `response.json()`自动将json字符串类型的响应内容转换为python对象（dict or list）
```python
import requests

# 目标url
url = 'https://www.baidu.com'
# 向目标url发送get请求
response = requests.get(url)
# 打印响应内容
# print(response.text)
# print(response.content.decode()) 			# 注意这里！
print(response.url)							# 打印响应的url
print(response.status_code)					# 打印响应的状态码
print(response.request.headers)				# 打印响应对象的请求头
print(response.headers)						# 打印响应头
print(response.request._cookies)			# 打印请求携带的cookies
print(response.cookies)						# 打印响应中携带的cookies
```

#### 3.6. 利用requests.session进行状态保持
```python
import requests
import re

# 构造请求头字典
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
}

# 实例化session对象
session = requests.session()

# 访问登陆页获取登陆请求所需参数
response = session.get('https://github.com/login', headers=headers)
authenticity_token = re.search('name="authenticity_token" value="(.*?)" />', response.text).group(1) # 使用正则获取登陆请求所需参数

# 构造登陆请求参数字典
data = {
    'commit': 'Sign in', # 固定值
    'utf8': '✓', # 固定值
    'authenticity_token': authenticity_token, # 该参数在登陆页的响应内容中
    'login': input('输入github账号：'),
    'password': input('输入github账号：')
}

# 发送登陆请求（无需关注本次请求的响应）
session.post('https://github.com/session', headers=headers, data=data)

# 打印需要登陆后才能访问的页面
response = session.get('https://github.com/1596930226', headers=headers)
print(response.text)

```

> requests模块中的Session类能够自动处理发送请求获取响应过程中产生的cookie，进而达到状态保持的目的。接下来我们就来学习它

##### 1 requests.session的作用以及应用场景

- requests.session的作用
  - 自动处理cookie，即 **下一次请求会带上前一次的cookie**
- requests.session的应用场景
  - 自动处理连续的多次请求过程中产生的cookie

##### 2 requests.session使用方法

> session实例在请求了一个网站后，对方服务器设置在本地的cookie会保存在session中，下一次再使用session请求对方服务器的时候，会带上前一次的cookie

```python
session = requests.session() # 实例化session对象
response = session.get(url, headers, ...)
response = session.post(url, data, ...)
```

- session对象发送get或post请求的参数，与requests模块发送请求的参数完全一致


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