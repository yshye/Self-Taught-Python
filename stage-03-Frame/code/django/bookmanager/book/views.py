import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# 定义视图：提供书籍列表信息
from django.urls import reverse


def bool_list(request):
    url = reverse('book:test')
    print(url)
    return HttpResponse('index')


def test_project(request):
    return HttpResponse('OK!')


def index(request, value1, value2):
    # 构造上下文
    context = {'v1': value1, 'v2': value2}
    print(context)
    return render(request, 'book/index.html', context)


def test_get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    a_list = request.GET.getlist('a')
    print(a)
    print(b)
    print(a_list)
    return JsonResponse({'a': a, 'b': b, 'aList': a_list})


def test_form_post(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    a_list = request.POST.getlist('a')
    response_data = {'a': a, 'b': b, 'aList': a_list}
    print(response_data)
    return JsonResponse(response_data)


def test_json_post(request):
    json_str = request.body
    print(json_str)
    json_data = json.loads(json_str)
    a = json_data['a']
    b = json_data['b']
    a_list = json_data['aList']
    response_data = {'a': a, 'b': b, 'aList': a_list}
    print(response_data)
    return JsonResponse(response_data)


def test_headers(request):
    meta = request.META
    print(meta['CONTENT_LENGTH'])
    print(meta['CONTENT_TYPE'])
    print(meta['HTTP_ACCEPT'])
    print(meta['HTTP_ACCEPT_ENCODING'])
    # print(meta['HTTP_ACCEPT_LANGUAGE'])
    print(meta['HTTP_HOST'])
    # print(meta['HTTP_REFERER'])
    print(meta['HTTP_USER_AGENT'])
    print(meta['QUERY_STRING'])
    print(meta['REMOTE_ADDR'])
    print(meta['REMOTE_HOST'])
    # print(meta['REMOTE_USER'])
    print(meta['REQUEST_METHOD'])
    print(meta['SERVER_NAME'])
    print(meta['SERVER_PORT'])

    headers_data = request.headers
    print(type(headers_data))
    a = headers_data.get('a')
    b = headers_data.get('b')
    a_list = headers_data.get('aList')
    response_data = {'a': a, 'b': b, 'aList': a_list}
    print(response_data)
    return JsonResponse(response_data)
