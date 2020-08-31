import json

import requests
from urllib3.exceptions import InsecureRequestWarning

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41'
}


def test_ssl():
    url = "https://sam.huat.edu.cn:8443/selfservice/"
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    response = requests.get(url, headers=headers, verify=False)
    print(response.content)


def test_proxy():
    url = 'http://www.baidu.com'
    free_proxy = {'http': '127.0.0.1:7890'}
    # 发送的数据
    response = requests.get(url=url, headers=headers, proxies=free_proxy)
    print(response)


def test_get_json():
    url = 'https://api.github.com/user'
    response = requests.get(url, headers=headers)
    data = response.content.decode('utf-8')
    data_dict = json.loads(data)
    print(type(data_dict))
    print(data_dict)
    print(data_dict['message'])
    print('-' * 100)
    data_json = response.json()
    print(type(data_json))
    print(data_json)
    print(data_json['message'])


def test_get_params():
    """参数自动转义"""
    url = "https://www.baidu.com/s"
    params = {'wd': '美女'}
    response = requests.get(url, headers=headers, params=params)
    content = response.content.decode('utf-8')
    with open('01_baidu.html', 'w', encoding='utf-8') as f:
        f.write(content)


class RequestSpider(object):
    def __init__(self):
        url = "http://www.baidu.com"
        self.response = requests.get(url, headers=headers)

    def run(self):
        data = self.response.content
        # 1. 获取请求头
        request_headers = self.response.request.headers
        print(request_headers)
        # 2. 获取响应头
        response_headers = self.response.headers
        print(response_headers)
        # 3. 响应状态码
        code = self.response.status_code
        print(code)
        # 4. 获取请求的cookie
        request_cookie = self.response.request._cookies
        print(request_cookie)
        # 5. 获取响应的cookie
        response_cookie = self.response.cookies
        print(response_cookie)


def test_get():
    r = requests.get('http://www.baidu.com')
    print(r)
    print(r.content)
    print(r.content.decode('utf-8'))


if __name__ == '__main__':
    # test_get()
    test_ssl()
    # test_proxy()
    # test_get_json()
    # test_get_params()
    # RequestSpider().run()
