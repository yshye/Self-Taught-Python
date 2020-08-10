import threading
import time

# 跳舞任务


def dance():
    for i in range(5):
        print(f"dance{i + 1}...doing...")
        time.sleep(0.1)


# 唱歌任务
def sing():
    for i in range(5):
        print(f"sing{i + 1}...doing...")
        time.sleep(0.1)


def task(count):
    for i in range(count):
        print(f"task{i + 1}...doing...")
        time.sleep(0.2)


# 定义全局变量
g_num = 0
# 创建全局互斥锁
lock = threading.Lock()


# 循环一次给全局变量加1
def sum_num1():
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    print(f"sum1:{g_num}")
    lock.release()


# 循环一次给全局变量加1
def sum_num2():
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num += 1
    print(f"sum2:{g_num}")
    lock.release()


if __name__ == '__main__':
    # 扩展： 获取当前线程
    # print("当前执行的线程为：", threading.current_thread())
    # 创建唱歌的线程
    # target： 线程执行的函数名
    sing_thread = threading.Thread(target=sing)
    # 创建跳舞的线程
    dance_thread = threading.Thread(target=dance)
    # args 表示以元组的方式给执行任务传参
    task_thead = threading.Thread(target=task, args=(3,), name='task')
    # kwargs 表示以字典方式给执行任务传参
    task2_thead = threading.Thread(target=task, kwargs={'count': 2}, name='task2')

    # 开启线程
    # sing_thread.start()
    # dance_thread.start()
    # task_thead.start()
    # task2_thead.start()

    # 创建两个线程
    first_thread = threading.Thread(target=sum_num1)
    second_thread = threading.Thread(target=sum_num2)
    # 启动线程
    first_thread.start()
    # 启动线程
    second_thread.start()
