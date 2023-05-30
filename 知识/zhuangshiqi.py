import time


def timer(func):
   def wrapper(*args, **kwargs):
       start_time = time.time()
       res = func(*args, **kwargs)
       exec_time = time.time() - start_time
       print(func.__name__, "执行时间", exec_time)
       return res
   return wrapper

@timer   # timer(add)
def add(x, y, **kwargs):
    print(kwargs)
    return x + y
print(add(x=1,y=2, zz=3))
print(add(1,2))

# 装饰器直接运行
print(timer(add)(1,2))



import datetime
import time
from functools import wraps
# 这是上下文管理的类
class Decorator:
    '''this is dec class '''
    def __init__(self, fn):
        if fn is not None:
            self.fn = fn
            # wraps(fn)(self)  # 这里是将fn的属性赋值给self实例，因为self实例会返回
    def __call__(self, *args, **kwargs):
        self.start = datetime.datetime.now()
        ret = self.fn(*args, **kwargs)
        self.interval = (datetime.datetime.now() - self.start).total_seconds()
        return 'interval is {}, result is {}'.format(self.interval, ret)
# 被装饰的函数
@Decorator    # add = Decorator(add)
def add(x,y):
    ''' this is a function '''
    time.sleep(2) # 延迟2秒
    return x + y
print(add(3,4))  # add调用的是Decorator的实例self，不是以前的函数add了

# Decorator(add)(3,4)
