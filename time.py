#pmj   2021-4-5  获取当前的日期和时间
import datetime

i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)
import datetime
aa = datetime.datetime.now().strftime("%y%m%d%H%M%S")
print(aa)
