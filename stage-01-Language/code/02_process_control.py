if __name__ == '__main__':
    #  条件控制
    age = 18
    # 婴儿(出生-1岁)、幼儿(1-4岁)、儿童(5-11)、少年(12-18)、青年(19-35)、中年(36-59)、老年(60以上)
    if age < 2:
        print('婴儿')
    elif age < 5:
        print('幼儿')
    elif age < 12:
        print('儿童')
    elif age < 19:
        print('少年')
    elif age < 36:
        print('青年')
    elif age < 60:
        print('中年')
    else:
        print('老年')

    # while循环
    index = 1
    while index < 5:
        print('第%d次打印' % index)
        index += 1

    index = 1
    while index < 5:
        if index == 3:
            print('第3次打印时退出循环')
            break
        print(f'第{index}次循环')
        index += 1
    else:
        print('执行while-else语句')

    index = 1
    while index < 5:
        if index == 4:
            print('第4次打印时跳过循环')
            index += 1
            continue
        print(f'第{index}次循环')
        index += 1
    else:
        print('执行while-else语句')

    # for循环
    items = [1, 2, 1, 3, 4, 121, 2]
    for item in items:
        print(item)
    else:
        print('执行for-else语句')
