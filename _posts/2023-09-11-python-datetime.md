---
title: "python中的有关时间的库的学习"

subtitle: "datetime/time/calendar模块"

author: "Painter"

date: 2023-09-11 16:13:00

tag:
    - PainterPython
    - Python
---

# 为什么学datetime/time库

其实工作中经常遇到这样的需求：

1. 把"2023-09-11 13:23:40"转化为时间戳。
2. 把时间戳的时间转为一个指定格式的字符串时间。

```python
import time
import datetime

# 第一个问题
t_str = "2023-09-11 13:23:40"
format_str = "%Y-%m-%d %H:%M:%S"

dt = datetime.datetime.strptime(t_str, format_str)
dt_tp = dt.timetuple()
t_stamps = time.mktime(dt_tp)
print(t_stamps)

# 第二个问题
```

# datetime库

这个库主要是关于时间和日期的库。

[官方API文档](https://docs.python.org/3/library/datetime.html)

该模块主要包括以下几个核心类和方法：

- 类
  - datetime.date：日期信息。
    - year
    - month
    - day
  - datetime.time：时间信息。
    - hour
    - minute
    - second
    - microsecond
    - tzinfo
  - datetime.datetime: 是date和time的组合。
    - year
    - month
    - day
    - hour
    - minute
    - second
    - microsecond
    - tzinfo
  - datetime.timedelta:任意两个日期、时间、日期时间或者毫秒间的差。
  - datetime.tzinfo：时区信息，抽象类。
  - datetime.timezone：时区信息，实现了tzinfo抽象基类。
- 属性
  - datetime.MINYEAR
  - datetime.MAXYEAR
  - datetime.UTC

下面我们分别来看下这几个类以及他们的主要函数

# time库

[官方文档](https://docs.python.org/3/library/time.html)

该模块提供了各种与时间相关的函数

## datetime.date
