from redis import *

if __name__ == '__main__':
    try:
        # 创建StrictRedis对象，与redis服务器建⽴连接
        sr = StrictRedis(host='127.0.0.1', port='6379', username='root', password='123456')
        # 输出响应结果，如果添加成功则返回True，否则返回False
        print(sr.set('name', 'yshye'))
        print(sr.get('name'))
        print(sr.set('name', 'JsonYe'))
        print(sr.get('name'))
        print(sr.delete('name'))
        print(sr.get('name'))
    except Exception as e:
        print(e)
