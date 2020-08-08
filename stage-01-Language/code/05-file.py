import os


def write(content='Hello Python'):
    # 1. 打开文件
    f = open('file/test.txt', 'w')
    # 2.文件写入
    f.write(content)
    # 3. 关闭文件
    f.close()


def read_lines():
    f = open('file/test.txt')
    content = f.readlines()
    print(content)
    # 关闭文件
    f.close()


def read_line():
    f = open('file/test.txt')
    content = f.readline()
    print(f'第一行：{content}')
    content = f.readline()
    print(f'第二行：{content}')
    # 关闭文件
    f.close()


def read_all_line():
    f = open('file/test.txt', 'r')
    for line in f:
        print(line)


# 将 “数字 文件名”格式的所有文件中的个位数前缀加‘0’
def add_zone(path):
    file_list = os.listdir(path)
    for file in file_list:
        str_list = file.split(' ')
        file_old = path + '/' + file
        if os.path.isdir(file_old):
            add_zone(file_old)
        else:
            if len(str_list[0]) == 1:
                file_new = path + '/0' + file
                print(file_new)
                # os.rename(file_old, file_new)
            else:
                print(file_old)


if __name__ == '__main__':
    # write("""Hello Python
    # Hello Java
    # Hello Flutter""")
    # read_lines()
    # read_line()
    # read_all_line()
    # add_zone(r'G:\Python\黑马Python\03 linux命令\2 linux命令（一）')
    add_zone(r'G:\Python\Node')
