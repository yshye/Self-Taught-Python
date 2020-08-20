from django.conf.urls import url
from book.views import *

app_name = 'book'
urlpatterns = [
    url(r'^(?P<value1>\d+)/(?P<value2>\d+)/$', index),
    # 匹配书籍列表信息的URL,调用对应的bookList视图
    url(r'^booklist/$', bool_list, name='index'),
    url(r'^testproject/$', test_project, name='test'),
    url(r'test_get', test_get),
    url(r'test_form_post', test_form_post),
    url(r'test_json_post', test_json_post),
    url(r'test_headers', test_headers),
]
