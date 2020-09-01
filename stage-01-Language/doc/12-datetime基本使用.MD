## datetime基本使用
### 1. 基本介绍
Python提供了多个内置模块用于操作日期时间，像calendar，time，datetime。time模块我在之前的文章已经有所介绍，它提供的接口与C标准库time.h基本一致。

相比于time模块，datetime模块的接口则更直观、更容易调用。

datetime模块定义了两个常量：datetime.MINYEAR和datetime.MAXYEAR，分别表示datetime所能表示的最小、最大年份。其中，MINYEAR = 1，MAXYEAR = 9999。
```python
import datetime
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
```

datetime模块定义了下面这几个类：

- datetime.timedelta：表示时间间隔，即两个时间点之间的长度。
- datetime.date：表示日期的类。常用的属性有year, month, day；
- datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond；
- datetime.datetime：表示日期时间。
- datetime.tzinfo：与时区有关的相关信息。（这里不详细充分讨论该类，感兴趣的童鞋可以参考python手册）

注：上面这些类型的对象都是不可变（immutable）的。

### 2. timedelta类
> 时间间隔

```python
from datetime import timedelta


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
# # 输出结果
# 最大间隔：999999999 days, 23:59:59.999999
# 最小间隔：-999999999 days, 0:00:00
# 最低间隔频率：0:00:00.000001
# 时间间隔：11 days, 1:10:34.003012
# 间隔天数:11
# 间隔天数检验:11
# 间隔秒数：4234
# 校验间隔秒数：4234
# 间隔微秒：3012
# 校验间隔微秒：3012
# 总间隔秒数：954634.003012
# 校验总间隔秒数：954634.003012
```

### 3. date类
#### 构造
date类表示一个日期。日期由年、月、日组成。date类的构造函数如下：
```python
datetime.date(year, month, day)
```
- year的范围是[MINYEAR, MAXYEAR]，即[1, 9999]；
- month的范围是[1, 12]。（月份是从1开始的，不是从0开始的）；
- day的最大值根据给定的year, month参数来决定。例如闰年2月份有29天；

#### 类常用方法与类属性
- date.max、date.min：date对象所能表示的最大、最小日期；
- date.resolution：date对象表示日期的最小单位。这里是天。
- date.today()：返回一个表示当前本地日期的date对象；
- date.fromtimestamp(timestamp)：根据给定的时间戮，返回一个date对象；
- datetime.fromordinal(ordinal)：将Gregorian日历时间转换为date对象；（Gregorian Calendar：一种日历表示方法，类似于我国的农历，西方国家使用比较多，此处不详细展开讨论。）

```python
from datetime import date, MINYEAR, MAXYEAR
def test():
    print('datetime.MINYEAR:%s' % MINYEAR)
    print('datetime.MAXYEAR:%s' % MAXYEAR)
    print('date.max:%s' % date.max)
    print('date.min:%s' % date.min)
    print('date.today():%s' % date.today())
if __name__ == '__main__':
    test()
# # ---- 结果 ----
# datetime.MINYEAR:1
# datetime.MAXYEAR:9999
# date.max:9999-12-31
# date.min:0001-01-01
# date.today():2020-09-01
```
#### 对象属性和方法

- date.year、date.month、date.day：年、月、日；
- date.replace(year, month, day)：生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性。（原有对象仍保持不变）
- date.timetuple()：返回日期对应的time.struct_time对象；
- date.toordinal()：返回日期对应的Gregorian Calendar日期；
- date.weekday()：返回weekday，如果是星期一，返回0；如果是星期2，返回1，以此类推；
- data.isoweekday()：返回weekday，如果是星期一，返回1；如果是星期2，返回2，以此类推；
- date.isocalendar()：返回格式如(year，month，day)的元组；
- date.isoformat()：返回格式如'YYYY-MM-DD’的字符串；
- date.strftime(fmt)：自定义格式化字符串。在下面详细讲解。

```python
from datetime import  date
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
    # 自定义格式化字符串
    print(f"now.strftime('%Y-%m-%d'):{now.strftime('%Y-%m-%d')}")
 
# # ---- 结果 ----
# now:2010-04-06,tomorrow:2010-04-07
# now.timetuple():time.struct_time(tm_year=2010, tm_mon=4, tm_mday=6, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=96, tm_isdst=-1)
# now.weekday():1
# now.isoweekday():2
# now.isocalendar():(2010, 14, 2)
# now.isoformat():2010-04-06
# now.strftime('%Y-%m-%d'):2010-04-06
```

#### 常用操作
```python
from datetime import date

def test_operation():
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
 
# # ---- 结果 ----
# now:2020-09-01,other:2020-09-03
# type(now - other):<class 'datetime.timedelta'>
# now - other:-2 days, 0:00:00
# 2020-08-30

```

### 4. time类
#### 构造
time类表示时间，由时、分、秒以及微秒组成。time类的构造函数如下：
```python
class datetime.time(hour[, minute[, second[, microsecond[, tzinfo]]]]) 

```
- hour:小时，[0,24)
- minute:分钟[0,60)
- second：秒[0,60)
- microsecond：微秒[0,1000000)
- tzinfo:时区信息

#### 类属性
- time.min、time.max：time类所能表示的最小、最大时间。其中，time.min = time(0, 0, 0, 0)， time.max = time(23, 59, 59, 999999)；
- time.resolution：时间的最小单位，这里是1微秒；
    
#### 实例方法和属性：
- time.hour、time.minute、time.second、time.microsecond：时、分、秒、微秒；
- time.tzinfo：时区信息；
- time.replace([hour[, minute[, second[, microsecond[, tzinfo]]]]])：创建一个新的时间对象，用参数指定的时、分、秒、微秒代替原有对象中的属性（原有对象仍保持不变）；
- time.isoformat()：返回型如"HH:MM:SS"格式的字符串表示；
- time.strftime(fmt)：返回自定义格式化字符串。在下面详细介绍；

### 5. datetime类
#### 构造
datetime是date与time的结合体，包括date与time的所有信息。它的构造函数如下：

```python
datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
```
#### 类属性与方法
- datetime.min、datetime.max：datetime所能表示的最小值与最大值；
- datetime.resolution：datetime最小单位；
- datetime.today()：返回一个表示当前本地时间的datetime对象；
- datetime.now([tz])：返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间；
- datetime.utcnow()：返回一个当前utc时间的datetime对象；
- datetime.fromtimestamp(timestamp[, tz])：根据时间戮创建一个datetime对象，参数tz指定时区信息；
- datetime.utcfromtimestamp(timestamp)：根据时间戮创建一个datetime对象；
- datetime.combine(date, time)：根据date和time，创建一个datetime对象；
- datetime.strptime(date_string, format)：将格式字符串转换为datetime对象

#### 对象属性与方法
- datetime.year、month、day、hour、minute、second、microsecond、tzinfo：
- datetime.date()：获取date对象；
- datetime.time()：获取time对象；
- datetime.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]])：
- datetime.timetuple()
- datetime.utctimetuple()
- datetime.toordinal()
- datetime.weekday()
- datetime.isocalendar()
- datetime.isoformat([sep])
- datetime.ctime()：返回一个日期时间的C格式字符串，等效于time.ctime(time.mktime(dt.timetuple()))；
- datetime.strftime(format)