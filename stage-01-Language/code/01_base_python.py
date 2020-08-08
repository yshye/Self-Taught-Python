"""
    多行注释
"""

# 单行注释

# 数据类型
if __name__ == '__main__':
    v1 = 1  # 整型 int
    print(type(v1))
    v2 = True  # 布尔  bool
    print(type(v2))
    v3 = 1.100000001  # 浮点型 float
    print(type(v3))
    v4 = 'abs'  # 字符串 str
    print(type(v4))
    v5 = {1, 2, 3}  # 集合 set
    print((type(v5)))
    v6 = [1, 2, 3]  # 列表 list
    print(type(v6))
    v7 = {'name': 'JsonYe', 'man': True, 'age': 20}  # 词典 dict
    print(type(v7))
    v8 = 1, 2, 3  # 元组  tuple, 等价 v8 = (1,2,3)
    print(type(v8))

    #  输出
    age = 18
    name = 'TOM'
    weight = 75.5
    student_id = 1

    # 我的名字是TOM
    print('我的名字是%s' % name)

    # 我的学号是0001
    print('我的学号是%04d' % student_id)

    # 我的体重是75.50公斤
    print('我的体重是%.2f公斤' % weight)

    # 我的名字是TOM，今年18岁了
    print('我的名字是%s，今年%d岁了' % (name, age))

    # 我的名字是TOM，明年19岁了
    print('我的名字是%s，明年%d岁了' % (name, age + 1))

    # 我的名字是TOM，明年19岁了
    print(f'我的名字是{name}, 明年{age + 1}岁了')

    # 输入
    # content = input('输入内容')
    # print('你是输入的是%s,类型为%s' % (content, type(content)))

    # 数据类型转换
    # 1. float() -- 转换成浮点型
    num1 = 1
    print(float(num1))
    print(type(float(num1)))

    # 2. str() -- 转换成字符串类型
    num2 = 10
    print(type(str(num2)))

    # 3. tuple() -- 将一个序列转换成元组
    list1 = [10, 20, 30]
    print(tuple(list1))
    print(type(tuple(list1)))

    # 4. list() -- 将一个序列转换成列表
    t1 = (100, 200, 300)
    print(list(t1))
    print(type(list(t1)))

    # 5. eval() -- 将字符串中的数据转换成Python表达式原本类型
    str1 = '10'
    str2 = '[1, 2, 3]'
    str3 = '(1000, 2000, 3000)'
    print(type(eval(str1)))
    print(type(eval(str2)))
    print(type(eval(str3)))

    # 算数运算符
    print('算数运算符：加、减、乘、除、取整、取余、指数、括号')
    print(1 + 1)
    print(10 - 9)
    print(1 * 3)
    print(10 / 3)
    print(10 // 3)  # 取整
    print(10 % 3)  # 取余
    print(10 ** 3)
    print(10 - (3 - 6))

    # 赋值
    a1 = a2 = 1
    print(a1, end=' ')
    print(a2)
    b1, b2 = 2, 3
    print(b1, end=' ')
    print(b2)

    # 复合赋值运算符,+=、-=、*=、/=、//=、%=、**=
    a = 100
    a += 1
    # 输出101  a = a + 1,最终a = 100 + 1
    print(a)

    b = 2
    b *= 3
    # 输出6  b = b * 3,最终b = 2 * 3
    print(b)

    c = 10
    c += 1 + 2
    # 输出13, 先算运算符右侧1 + 2 = 3， c += 3 , 推导出c = 10 + 3
    print(c)

    # 比较运算符，==、!=、<、>、<=、>=
    a = 7
    b = 5
    print(a == b)  # False
    print(a != b)  # True
    print(a < b)  # False
    print(a > b)  # True
    print(a <= b)  # False
    print(a >= b)  # True

    # 逻辑运算符,and、 or、 not
    a = 1
    b = 2
    c = 3
    print((a < b) and (b < c))  # True
    print((a > b) and (b < c))  # False
    print((a > b) or (b < c))  # True
    print(not (a > b))  # True
