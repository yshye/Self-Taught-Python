import re
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

import requests


def test1():
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    print(html.read())


def test2():
    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
    # features = html.parser:Python标准库；=lxml:lxml HTML 解析器；= ["lxml-xml"]/"xml" lxml XML 解析器; =html5lib:html5lib解析
    html_bs = BeautifulSoup(html.read(), features="lxml")
    # 建议使用 lxml的解析，因为效率更高. 在Python2.7.3之前的版本和Python3中3.2.2之前的版本,必须安装lxml或html5lib, 因为那些Python版本的标准库中内置的HTML解析方法不够稳定.
    print(html_bs.h1)
    print(html_bs.html.body.h1)
    print(html_bs.html.h1)
    print(html_bs.body.h1)


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs_obj = BeautifulSoup(html.read(), 'lxml')
        title = bs_obj.body.h1
    except AttributeError as e:
        print(e)
        return None
    return title


def test3():
    title = get_title("http://www.pythonscraping.com/pages/page2.html")
    if title is None:
        print("Title could not be found")
    else:
        print(title)


def test_get_next():
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    bs_obj = BeautifulSoup(html, 'lxml')
    name_list = bs_obj.findAll("span", {"class": "green"})
    for name in name_list:
        print(name.get_text())


def print_list(items):
    for item in items:
        print(item)


def test_find_all():
    # html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    file = open('res/warandpeace.html', 'r')
    bs_obj = BeautifulSoup(file.read(), 'lxml')
    file.close()
    # name_list = bs_obj.findAll({'h1', 'h2', "h3", "h4", "h5"})
    # print_list(name_list)
    # name_list = bs_obj.findAll("span", {"class": {"green"}})
    # print_list(name_list)
    # name_list = bs_obj.findAll(text='the prince')
    # print(len(name_list))
    name_list = bs_obj.findAll(id='text')
    print(name_list[0].get_text())


def test_children():
    """处理子标签和其他后代标签"""
    file = open('res/page3.html', 'r', encoding='gbk')
    bs_obj = BeautifulSoup(file.read(), 'lxml')
    file.close()
    print_list(bs_obj.find("table", {"id": "giftList"}).children)


def test_next_siblings():
    """ 处理兄弟标签 """
    file = open('res/page3.html', 'r', encoding='gbk')
    bs_obj = BeautifulSoup(file.read(), 'lxml')
    file.close()
    print_list(bs_obj.find("table", {"id": "giftList"}).tr.next_siblings)


def test_parent_previous_sibling():
    """ 处理父标签 """
    file = open('res/page3.html', 'r', encoding='gbk')
    bs_obj = BeautifulSoup(file.read(), 'lxml')
    file.close()
    print(bs_obj.find("img", {"res": "./page3_files/img1.jpg"
                              }).parent.previous_sibling.get_text())


def test_find_img():
    file = open('res/page3.html', 'r', encoding='gbk')
    bs_obj = BeautifulSoup(file.read(), 'lxml')
    file.close()
    images = bs_obj.findAll('img', {'res': re.compile('./page3_files/img.*.jpg')})
    images = [item['res'] for item in images]
    print_list(images)


def test_lambda():
    file = open('res/page3.html', 'r', encoding='gbk')
    bs_obj = BeautifulSoup(file.read(), 'lxml')
    file.close()
    items = bs_obj.findAll(lambda tag: len(tag.attrs) == 2)
    print_list(items)


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test_get_next()
    # test_find_all()
    # test_children()
    # test_next_siblings()
    # test_parent_previous_sibling()
    # test_find_img()
    test_lambda()
