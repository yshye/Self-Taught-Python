if __name__ == '__main__':
    name = 'JsonYe'
    note = """
我是多行文本
这是第二行
    """
    print(name[0])
    print(name[3])
    # print(name[100])  # 下标越界，会抛出Error IndexError
    print(note[1])
    print(note[2])

    my_str = "hello world and itcast and itheima and Python"

    # 结果：hello world he itcast he itheima he Python
    print(my_str.replace('and', 'he'))
    # 结果：hello world he itcast he itheima he Python
    print(my_str.replace('and', 'he', 2))
    # 结果：hello world and itcast and itheima and Python
    print(my_str)

    # 结果：['hello world ', ' itcast ', ' itheima ', ' Python']
    print(my_str.split('and'))
    # 结果：['hello world ', ' itcast ', ' itheima and Python']
    print(my_str.split('and', 2))
    # 结果：['hello', 'world', 'and', 'itcast', 'and', 'itheima', 'and', 'Python']
    print(my_str.split(' '))
    # 结果：['hello', 'world', 'and itcast and itheima and Python']
    print(my_str.split(' ', 2))

    name = "abcdefg"
    print(f"{name}.name[2:5:1] = {name[2:5:1]}")
    print(f"{name}.name[:5] = {name[:5]}")
    print(f"{name}.name[1:] = {name[1:]}")
    print(f"{name}.name[:] = {name[:]}")
    print(f"{name}.name[::2] = {name[::2]}")
    print(f"{name}.name[:-1] = {name[:-1]}")
    print(f"{name}.name[-4:-1] = {name[-4:-1]}")
    print(f"{name}.name[::-1] = {name[::-1]}")

    print(f"{name}.count('b') = {name.count('b')}")



