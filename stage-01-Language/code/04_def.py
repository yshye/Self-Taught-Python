def sum(num1, num2):
    """
    计算两数之和
    :param num1: 数字1
    :param num2: 数字2
    :return: 两数之和
    """
    return num1 + num2


a = 100


def f1():
    print(a)  # 此时为全局变量


def f2():
    a = 200
    print(a)  # 此时为局部变量


def f3():
    global a
    a = 200
    print(a)  # 此时为全局变量变量


def factorial(max):
    if max == 1:
        return 1
    else:
        return factorial(max - 1) * max


if __name__ == '__main__':
    print(sum(12, 23))

    f1()  # 100
    f2()  # 200
    print(a)  # 100
    f3()  # 200
    print(a)  # 200

    print(factorial(4))
