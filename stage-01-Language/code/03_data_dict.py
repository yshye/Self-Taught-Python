if __name__ == '__main__':
    dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
    print(dict1['name'])  # 不存在name时，会报错
    print(dict1.get('name'))  # 不存在name时，返回None
    print(dict1.keys())  # 查询所有的key dict_keys(['name', 'age', 'gender'])
    print(dict1.values())  # 查询所有的value dict_values(['Tom', 20, '男'])
    print(dict1.items())  # dict_items([('name', 'Tom'), ('age', 20), ('gender', '男')])

    # 遍历
    for key in dict1.keys():
        print(key)

    for value in dict1.values():
        print(value)

    for item in dict1.items():
        print(item)

    for key, value in dict1.items():
        print(f'{key} = {value}')
