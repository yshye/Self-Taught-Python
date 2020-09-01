from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_content():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path='res/chromedriver.exe', options=chrome_options)
    driver.get('http://www.itcast.cn/')
    print(driver.page_source)
    ret = driver.find_elements_by_tag_name('h2')
    print(ret[0].text)  #
    ret = driver.find_elements_by_link_text('黑马程序员')
    print(ret[0].get_attribute('href'))
    driver.quit()


def test_selenium_headless():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path='res/chromedriver.exe', options=chrome_options)
    driver.get("https://www.baidu.com")
    print(driver.page_source)
    driver.save_screenshot("baidu.png")
    driver.close()


# PhantomJS 是一个基于Webkit的“无界面”(headless)浏览器，它会把网站加载到内存并执行页面上的 JavaScript。下载地址：<http://phantomjs.org/download.html>
def test_phantomjs():
    # 指定driver的绝对路径
    driver = webdriver.PhantomJS(executable_path='res/phantomjs')
    # Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead
    # selenium已经放弃PhantomJS，了，建议使用火狐或者谷歌无界面浏览器
    # Selenium support for PhantomJS has been deprecated, please use headless
    # driver = webdriver.Chrome(executable_path='/home/worker/Desktop/driver/chromedriver')

    # 向一个url发起请求
    driver.get("http://www.itcast.cn/")

    # 把网页保存为图片
    driver.save_screenshot("itcast.png")

    # 退出模拟浏览器
    driver.quit()  # 一定要退出！不退出会有残留进程！


def test_selenium():
    # 如果driver没有添加到了环境变量，则需要将driver的绝对路径赋值给executable_path参数
    driver = webdriver.Chrome(executable_path='res/chromedriver')

    # 如果driver添加了环境变量则不需要设置executable_path
    # driver = webdriver.Chrome()

    # 向一个url发起请求
    driver.get("http://www.itcast.cn/")

    # 把网页保存为图片，69版本以上的谷歌浏览器将无法使用截图功能
    # driver.save_screenshot("itcast.png")

    print(driver.title)  # 打印页面的标题

    # 退出模拟浏览器
    driver.quit()  # 一定要退出！不退出会有残留进程！


if __name__ == '__main__':
    test_content()
