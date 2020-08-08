from random import randint

if __name__ == '__main__':
    """
    需求：有三个办公室，8位老师，8位老师随机分配到3个办公室
    """

    room_teacher: [[str]] = [[], [], []]

    for index in range(9):
        room_index = randint(0, 2)
        room_teacher[room_index].append('老师%d' % (index + 1))
    print(room_teacher)
