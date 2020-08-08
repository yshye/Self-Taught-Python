# 现在有一列表 lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] ，求出 1/4/7 和 1/5/9元素，思考如何取出

if __name__ == '__main__':
    lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    lst1 = [lst[i][0] for i in range(len(lst))]
    print(lst1)
    lst2 = [lst[i][i] for i in range(len(lst))]
    print(lst2)
    # 创建 [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    lst = [(i, j) for i in range(1, 3) for j in range(3)]
    print(lst)
    a = [lambda x: x * i for i in range(3)]
    print(type(a))
    print(a[0](2))
    print(a[1](2))
    print(a[2](2))

    dict1 = {'name': 'yshye', 'age': 20, 'sex': '男'}
    print(dict1)
    dict2 = {key: value for value, key in dict1.items()}
    print(dict2)

    dict_a = {key: value for key in 'python' for value in range(2)}
    print(dict_a)

    # 可以根据键来构造值
    dict_b = {key: key * key for key in range(6)}
    print(dict_b)

    # 遍历一个有键值关系的可迭代对象
    list_phone = [('HUAWEI', '华为'), ('MI', '小米'), ('OPPO', 'OPPO'), ('VIVO', 'VIVO')]
    dict_c = {key: value for value, key in list_phone}
    print(dict_c)
    dict_c = {key: value for key, value in list_phone}
    print(dict_c)

    dict1 = {key: value for key in range(8) for value in range(8)}
    print(dict1)

    set1 = {i for i in range(1, 11)}
    print(set1)

    set2 = {i for i in range(1, 11) if i % 2 == 0}
    print(set2)
