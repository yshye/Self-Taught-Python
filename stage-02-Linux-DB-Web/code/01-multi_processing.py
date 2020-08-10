import multiprocessing
import os
import time


# 跳舞任务
def dance():
    # 获取当前进程的编号
    print("sing:", os.getpid())
    # 获取当前进程
    print("sing:", multiprocessing.current_process())
    # 获取父进程的编号
    print(f"【{multiprocessing.current_process().name}】的父进程编号:", os.getppid())
    for i in range(5):
        print("dance...doing...")
        time.sleep(0.1)


# 唱歌任务
def sing():
    # 获取当前进程的编号
    print("sing:", os.getpid())
    # 获取当前进程
    print("sing:", multiprocessing.current_process())
    # 获取父进程的编号
    print(f"【{multiprocessing.current_process().name}】的父进程编号:", os.getppid())
    for i in range(5):
        print(f"sing{i + 1}...doing...")
        time.sleep(0.1)


def task(count):
    # 获取当前进程的编号
    print("task:", os.getpid())
    # 获取当前进程
    print("task:", multiprocessing.current_process())
    # 获取父进程的编号
    name = multiprocessing.current_process().name
    print(f"【{name}】的父进程编号:", os.getppid())
    for i in range(count):
        print(f"task{i + 1}...{name}.doing...")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建跳舞的子进程
    # group: 表示进程组，目前只能使用None; assert group is None, 'group argument must be None for now'
    # target: 表示执行的目标任务名(函数名、方法名)
    dance_process = multiprocessing.Process(target=dance, name="dance")
    # name: 进程名称, 默认是Process-1, .....
    sing_process = multiprocessing.Process(target=sing)
    # args 表示以元组的方式给执行任务传参
    task_process = multiprocessing.Process(target=task, args=(3,), name='task')
    # kwargs 表示以字典方式给执行任务传参
    task2_process = multiprocessing.Process(target=task, kwargs={'count': 2}, name='task2')

    # 启动子进程执行对应的任务
    dance_process.start()
    sing_process.start()
    task_process.start()
    task2_process.start()
