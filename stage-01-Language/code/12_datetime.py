from datetime import date, timedelta


def test_timedelta():
    print(f"最大间隔：{timedelta.max}")
    print(f"最小间隔：{timedelta.min}")
    print(f"最低间隔频率：{timedelta.resolution}")
    weeks, days, hours, minutes, seconds, milliseconds, microseconds = 1, 2, 48, 70, 34, 3, 12
    # 3天的间隔
    interval = timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds,
                         milliseconds=milliseconds, microseconds=microseconds)
    print(f"时间间隔：{interval}")
    print(f"间隔天数:{interval.days}")
    print(
        "间隔天数检验:%d" % (weeks * 7 + days + hours / 24 + minutes / (24 * 60) + seconds / (24 * 60 * 60) + milliseconds / (
                24 * 60 * 60 * 1000) + microseconds / (24 * 60 * 60 * 1000 * 1000)))
    print(f"间隔秒数：{interval.seconds}")
    print(f"校验间隔秒数：{minutes * 60 + seconds}")
    print(f"间隔微秒：{interval.microseconds}")
    print(f"校验间隔微秒：{milliseconds * 1000 + microseconds}")
    print(f"总间隔秒数：{interval.total_seconds()}")
    print("校验总间隔秒数：%0.6f" % ((((((((weeks * 7) + days) * 24) + hours) * 60) + minutes) * 60 + seconds) + (
            milliseconds * 1000 + microseconds) / 1000000))


def test_date_operation():
    now = date.today()
    other = now.replace(day=3)
    print(f"now:{now},other:{other}")
    # 日期相减得到日期间隔
    interval = now - other
    print(f"type(now - other):{type(interval)}")
    print(f"now - other:{interval}")
    # 日期+间隔得到新日期
    now2 = now + interval
    print(now2)


def test_date_object():
    now = date(2010, 4, 6)
    # 生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性。（原有对象仍保持不变）
    tomorrow = now.replace(day=7)
    print(f"now:{now},tomorrow:{tomorrow}")
    # 返回日期对应的time.struct_time对象；
    print(f"now.timetuple():{now.timetuple()}")
    # 返回weekday，如果是星期一，返回0；如果是星期2，返回1，以此类推；
    print(f"now.weekday():{now.weekday()}")
    # 返回weekday，如果是星期一，返回1；如果是星期2，返回2，以此类推；
    print(f"now.isoweekday():{now.isoweekday()}")
    # 返回格式如(year，month，day)的元组；
    print(f"now.isocalendar():{now.isocalendar()}")
    # 返回格式如'YYYY-MM-DD’的字符串；
    print(f"now.isoformat():{now.isoformat()}")
    # 自定义格式化字符串de
    print(f"now.strftime('%Y-%m-%d'):{now.strftime('%Y-%m-%d')}")


def test_date_init():
    n_date = date(2020, month=3, day=21)
    print(n_date)


def test_date_class():
    print('date.max:%s' % date.max)
    print('date.min:%s' % date.min)
    print('date.today():%s' % date.today())


if __name__ == '__main__':
    # test_date_class()
    # test_date_init()
    # test_date_object()
    # test_date_operation()
    test_timedelta()
