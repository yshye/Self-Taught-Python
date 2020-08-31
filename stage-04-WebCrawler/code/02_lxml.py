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
