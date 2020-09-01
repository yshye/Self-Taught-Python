## XPath基础及lxml解析库

[<< 返回目录](../README.MD)


> XPath 是一门在 XML 文档中查找信息的语言。XPath 用于在 XML 文档中通过元素和属性进行导航。

## XPath
### 1. XPath简介
> XPath，全称 XML Path Language，即 XML 路径语言，它是一门在 XML 文档中查找信息的语言。最初是用来搜寻 XML 文档的，但同样适用于 HTML 文档的搜索。所以在做爬虫时完全可以使用 XPath 做相应的信息抽取。

#### 1.1 什么是XPath
- XPath 使用路径表达式在 XML 文档中进行导航
- XPath 包含一个标准函数库
- XPath 是 XSLT 中的主要元素
- XPath 是一个 W3C 标准

#### 1.2 XPath 路径表达式
XPath 使用路径表达式来选取 XML 文档中的节点或者节点集。这些路径表达式和我们在常规的电脑文件系统中看到的表达式非常相似。

#### 1.3 XPath 标准函数
XPath 含有超过 100 个内建的函数。这些函数用于字符串值、数值、日期和时间比较、节点和 QName 处理、序列处理、逻辑值等等。

### 2. 节点
在 XPath 中，有七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档（根）节点。XML 文档是被作为节点树来对待的。树的根被称为文档节点或者根节点。

#### 2.1 节点（Node）
请看下面这个 XML 文档：
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<bookstore>
<book>
  <title lang="en">Harry Potter</title>
  <author>J K. Rowling</author> 
  <year>2005</year>
  <price>29.99</price>
</book>
</bookstore>
```
— 上面的XML文档中的节点例子：
```text
<bookstore> （文档节点）
<author>J K. Rowling</author> （元素节点）
lang="en" （属性节点） 
```
#### 2.2 基本值或原子值（Atomic value）
基本值是无父或无子的节点。
基本值的例子：
```text
J K. Rowling
"en"
```
#### 2.3 项目（Item）
项目是基本值或者节点。

#### 2.4 节点关系-父节点（Parent）
每个元素以及属性都有一个父。

在下面的例子中，book 元素是 title、author、year 以及 price 元素的父：
```xml
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```
#### 2.4 节点关系-子（Children）
元素节点可有零个、一个或多个子。

在下面的例子中，title、author、year 以及 price 元素都是 book 元素的子：
```xml
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```


#### 2.4 节点关系-同胞（Sibling）
拥有相同的父的节点

在下面的例子中，title、author、year 以及 price 元素都是同胞：

```xml
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```

#### 2.4 节点关系-先辈（Ancestor）
某节点的父、父的父，等等。

在下面的例子中，title 元素的先辈是 book 元素和 bookstore 元素：

```xml
<bookstore>

<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

</bookstore>
```

#### 2.4 节点关系-后代（Descendant）
某个节点的子，子的子，等等。

在下面的例子中，bookstore 的后代是 book、title、author、year 以及 price 元素：
```xml
<bookstore>

<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

</bookstore>
```

### 3. 语法
> XPath 使用路径表达式来选取 XML 文档中的节点或节点集。节点是通过沿着路径 (path) 或者步 (steps) 来选取的。
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>

<bookstore>

<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>
```
#### 3.1 选取节点
XPath 使用路径表达式在 XML 文档中选取节点。节点是通过沿着路径或者 step 来选取的。

下面列出了最有用的路径表达式：

表达式 |	描述
---|---
`nodename`|	选取此节点的所有子节点。
`/`	|从根节点选取。
`//`	|从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
`.`	|选取当前节点。
`..`	|选取当前节点的父节点。
`@`	|选取属性。

#####  实例
在下面的表格中，我们已列出了一些路径表达式以及表达式的结果：

路径表达式	|结果
---|---
`bookstore`	|选取 bookstore 元素的所有子节点。
`/bookstore`	|选取根元素 bookstore。<br/>注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！
`bookstore/book`	|选取属于 bookstore 的子元素的所有 book 元素。
`//book`|选取所有 book 子元素，而不管它们在文档中的位置。
`bookstore//book`	|选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。
`//@lang`	|选取名为 lang 的所有属性。

#### 3.2 谓语（Predicates）
谓语用来查找某个特定的节点或者包含某个指定的值的节点。

谓语被嵌在方括号中。

##### 实例
在下面的表格中，我们列出了带有谓语的一些路径表达式，以及表达式的结果：

路径表达式	|结果
---|---
`/bookstore/book[1]`	|选取属于 bookstore 子元素的第一个 book 元素。
`/bookstore/book[last()]`	|选取属于 bookstore 子元素的最后一个 book 元素。
`/bookstore/book[last()-1]`	|选取属于 bookstore 子元素的倒数第二个 book 元素。
`/bookstore/book[position()<3]`	|选取最前面的两个属于 bookstore 元素的子元素的 book 元素。
`//title[@lang]`	|选取所有拥有名为 lang 的属性的 title 元素。
`//title[@lang='eng']`	|选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。
`/bookstore/book[price>35.00]`	|选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。
`/bookstore/book[price>35.00]/title`	|选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。

#### 3.3 选取未知节点
XPath 通配符可用来选取未知的 XML 元素。

通配符	|描述
---|---
`*`	|匹配任何元素节点。
`@*`	|匹配任何属性节点。
`node()`	|匹配任何类型的节点。

##### 实例
在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：

路径表达式	|结果
---|---
`/bookstore/*`	|选取 bookstore 元素的所有子元素。
`//*`	|选取文档中的所有元素。
`//title[@*]`	|选取所有带有属性的 title 元素。

#### 3.4 选取若干路径
通过在路径表达式中使用“|”运算符，您可以选取若干个路径。

##### 实例
在下面的表格中，我们列出了一些路径表达式，以及这些表达式的结果：

路径表达式	|结果
---|---
//book/title &#124; //book/price	|选取 book 元素的所有 title 和 price 元素。
//title &#124; //price	|选取文档中的所有 title 和 price 元素。
/bookstore/book/title &#124; //price	|选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。

### 4. 轴
#### 4.1 轴可定义相对于当前节点的节点集

轴名称	|结果
---|---
ancestor	|选取当前节点的所有先辈（父、祖父等）。
ancestor-or-self	|选取当前节点的所有先辈（父、祖父等）以及当前节点本身。
attribute	|选取当前节点的所有属性。
child	|选取当前节点的所有子元素。
descendant	|选取当前节点的所有后代元素（子、孙等）。
descendant-or-self	|选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
following	|选取文档中当前节点的结束标签之后的所有节点。
namespace	|选取当前节点的所有命名空间节点。
parent	|选取当前节点的父节点。
preceding	|选取文档中当前节点的开始标签之前的所有节点。
preceding-sibling	|选取当前节点之前的所有同级节点。
self	|选取当前节点。

#### 4.2 路径
- 绝对位置路径：
`/step/step/...`
- 相对位置路径：
`step/step/...`


#### 4.3 步
- 轴（axis）

定义所选节点与当前节点之间的树关系
- 节点测试（node-test）

识别某个轴内部的节点
- 零个或者更多谓语（predicate）

更深入地提炼所选的节点集

##### 步的语法：
```text
轴名称::节点测试[谓语]
```

##### 示例
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>

<bookstore>

<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>
```
例子	|结果
---|---
child::book	|选取所有属于当前节点的子元素的 book 节点。
attribute::lang	|选取当前节点的 lang 属性。
child::*	|选取当前节点的所有子元素。
attribute::*	|选取当前节点的所有属性。
child::text()	|选取当前节点的所有文本子节点。
child::node()	|选取当前节点的所有子节点。
descendant::book	|选取当前节点的所有 book 后代。
ancestor::book	|选择当前节点的所有 book 先辈。
ancestor-or-self::book	|选取当前节点的所有 book 先辈以及当前节点（如果此节点是 book 节点）
child::*/child::price	|选取当前节点的所有 price 孙节点。

### 5. 运算符
运算符	|描述	|实例	|返回值
---|---|---|---
&#124;	|计算两个节点集	|//book &#124; //cd	|返回所有拥有 book 和 cd 元素的节点集
`+`	|加法	|6 + 4	|10
`-`	|减法	|6 - 4	|2
`*`	|乘法	|6 * 4	|24
`div`	|除法	|8 div 4	|2
`=`	|等于	|price=9.80	|如果 price 是 9.80，则返回 true。<br/>如果 price 是 9.90，则返回 false。
`!=`	|不等于	|price!=9.80 |如果 price 是 9.90，则返回 true。<br/>如果 price 是 9.80，则返回 false。
`<`	|小于	|price<9.80	|如果 price 是 9.00，则返回 true。<br/>如果 price 是 9.90，则返回 false。
`<=`	|小于或等于	|price<=9.80	|如果 price 是 9.00，则返回 true。<br/>如果 price 是 9.90，则返回 false。
`>`	|大于	|price>9.80	|如果 price 是 9.90，则返回 true。<br/>如果 price 是 9.80，则返回 false。
`>=`	|大于或等于	|price>=9.80	|如果 price 是 9.90，则返回 true。<br/>如果 price 是 9.70，则返回 false。
`or`	|或	|price=9.80 or price=9.70	|如果 price 是 9.80，则返回 true。<br/>如果 price 是 9.50，则返回 false。
`and`	|与	|price>9.00 and price<9.90	|如果 price 是 9.80，则返回 true。<br/>如果 price 是 8.50，则返回 false。
`mod`	|计算除法的余数|	5 mod 2	|1

### 6. 实例
- "books.xml"
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>

<bookstore>

<book category="COOKING">
  <title lang="en">Everyday Italian</title>
  <author>Giada De Laurentiis</author>
  <year>2005</year>
  <price>30.00</price>
</book>

<book category="CHILDREN">
  <title lang="en">Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

<book category="WEB">
  <title lang="en">XQuery Kick Start</title>
  <author>James McGovern</author>
  <author>Per Bothner</author>
  <author>Kurt Cagle</author>
  <author>James Linn</author>
  <author>Vaidyanathan Nagarajan</author>
  <year>2003</year>
  <price>49.99</price>
</book>

<book category="WEB">
  <title lang="en">Learning XML</title>
  <author>Erik T. Ray</author>
  <year>2003</year>
  <price>39.95</price>
</book>

</bookstore>
```

## lxml解析库
### 1. 简介
> lxml 是 一个HTML/XML的解析器，主要的功能是如何解析和提取 HTML/XML 数据。
>
>lxml和正则一样，也是用 C 实现的，是一款高性能的 Python HTML/XML 解析器，我们可以利用之前学习的XPath语法，来快速的定位特定元素以及节点信息。

### 2. 安装
需要安装C语言库
```shell script
pip install lxml
```

### 3. 自动补全
```python
# 使用 lxml 的 etree 库
from lxml import etree 

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签
     </ul>
 </div>
'''

#利用etree.HTML，将字符串解析为HTML文档
html = etree.HTML(text) 

# 按字符串序列化HTML文档
result = etree.tostring(html)
print(type(result))
print(result.decode())
```
输出结果：
```html
<html><body>
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
 </div>
</body></html>
```

### 4. 实例
```python
## lxml基本使用
from lxml import etree

text = '''
   <div>
       <ul>
            <li class="item-0"><a href="link1.html">first item</a></li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-inactive"><a href="link3.html">third item</a></li>
            <li class="item-1"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个</>闭合标签
        </ul>
    </div>
   '''


def test_etree():
    # 利用etree.HTML，将字符串解析为HTML文档
    html = etree.HTML(text)
    # 按字符串序列化HTML文档
    result = etree.tostring(html)
    print(type(result))
    print(result.decode())


def test_node_all():
    html = etree.HTML(text)
    result = html.xpath('//*')
    print(result)


def test_node_li():
    html = etree.HTML(text)
    result = html.xpath('//li')
    print(result)


def test_node_child():
    html = etree.HTML(text)
    result = html.xpath('//li/a')
    print(result)


def test_node_parent():
    html = etree.HTML(text)
    result = html.xpath('//a[@href="link4.html"]/../@class')
    print(result)
    result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
    print(result)


# 匹配时可以用@符号进行属性过滤：
def test_active():
    html = etree.HTML(text)
    print_line('@过滤器')
    result = html.xpath('//li[@class="item-inactive"]')
    print(result)
    # @符号相当于过滤器，可以直接获取节点的属性值：
    result = html.xpath('//li/a/@href')
    print(result)
    # 有时候，某些节点的某个属性可能有多个值：
    print_line('属性有多个值')
    text_test = '''
    <li class="li li-first"><a href="link.html">first item</a></li>
    '''
    html = etree.HTML(text_test)
    result = html.xpath('//li[contains(@class, "li")]/a/text()')
    print(result)
    # 当前节点有多个属性时，需要同时进行匹配：
    print_line('节点多个属性')
    text_test = '''
    <li class="li li-first" name="item"><a href="link.html">first item</a></li>
    '''
    html = etree.HTML(text_test)
    result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
    print(result)
    # 按序选择
    print_line('按序选择')
    # 匹配结果有多个节点，需要选中第二个或最后一个，可以按照中括号内加索引或其他相应语法获得：
    html = etree.HTML(text)
    # 获取第一个
    result = html.xpath('//li[1]/a/text()')
    print(result)
    # 获取最后一个
    result = html.xpath('//li[last()]/a/text()')
    print(result)
    # 获取前两个
    result = html.xpath('//li[position()<3]/a/text()')
    print(result)
    # 获取倒数第三个
    result = html.xpath('//li[last()-2]/a/text()')
    print(result)


def test_node():
    html = etree.HTML(text)
    # 获取所有祖先节点
    result = html.xpath('//li[1]/ancestor::*')
    print(result)
    # 获取 div 祖先节点
    result = html.xpath('//li[1]/ancestor::div')
    print(result)
    # 获取当前节点所有属性值
    result = html.xpath('//li[1]/attribute::*')
    print(result)
    # 获取 href 属性值为 link1.html 的直接子节点
    result = html.xpath('//li[1]/child::a[@href="link1.html"]')
    print(result)
    # 获取所有的的子孙节点中包含 span 节点但不包含 a 节点
    result = html.xpath('//li[1]/descendant::span')
    print(result)
    # 获取当前所有节点之后的第二个节点
    result = html.xpath('//li[1]/following::*[2]')
    print(result)
    # 获取当前节点之后的所有同级节点
    result = html.xpath('//li[1]/following-sibling::*')
    print(result)


def print_line(title):
    print("-" * 25, end='')
    print(title, end='')
    print("-" * 25)


# 获取文本
def test_text():
    html = etree.HTML(text)
    # 一是获取文本所在节点后直接获取文本
    result = html.xpath("//li[@class='item-0']/a/text()")
    print(result)
    # 二是使用 // 获取。获取到补全代码时换行产生的特殊字符。
    result = html.xpath("//li[@class='item-0']//text()")
    print(result)


if __name__ == '__main__':
    # test_etree()
    # test_node_all()
    # test_node_li()
    # test_node_child()
    # test_node_parent()
    # test_active()
    # test_text()
    test_node()

```



