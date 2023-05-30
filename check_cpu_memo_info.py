import psutil
import datetime
import time
from pylab import *
cpu_list = []
memory_list = []
root_list = []
network_rec = []
network_send = []
time_list = []























def func1():
    # CPU的核数
    cpu_count = psutil.cpu_count(logical=False)
    # CPU逻辑核数
    # cpu_count = psutil.cpu_count()
    # cpu的使用率
    cup_per = psutil.cpu_percent(interval=1)  # 0.5刷新频率
    # print(f"cpu的逻辑核数为{cpu_count}, cpu的平均使用率为{cup_per}")
    if len(cpu_list) > 10:
        del cpu_list[0]
    cpu_list.append(cup_per)
    # 内存信息
    memory_info = psutil.virtual_memory()
    # 总内存
    memory_total = memory_info.total / 1024 / 1024 / 1024
    memory_per = memory_info.percent
    # print(f"总内存大小为{round(memory_total, 2)}G,内存的使用率为{memory_per}")
    if len(memory_list) > 10:
        del memory_list[0]
    memory_list.append(memory_per)

    # 硬盘信息
    disk_info = psutil.disk_usage("/")  # 根目录磁盘信息
    # print(disk_info)
    # 根目录大小
    disk_total = disk_info.total
    # 根目录使用情况
    disk_per = float(disk_info.used / disk_total * 100)
    # print(f"根目录大小为{round(disk_total / 1024 / 1024 / 1024, 2)}G，根目录使用率为{round(disk_per, 2)}")

    if len(root_list) > 10:
        del root_list[0]
    root_list.append(round(disk_per, 2))
    # 网络使用情况
    net = psutil.net_io_counters()
    # print(net)
    # 网卡配置信息
    net_ipy = psutil.net_if_addrs()
    # print(f"net_ipy {net_ipy}")
    # net_ip = list(net_ipy['以太网 3'][1])[1]  # 根据自己网卡修改
    # print(f"本机的IP地址为{net_ip}")
    # 收取数据
    net_recv = float(net.bytes_recv / 1024 / 1024)
    # 发送数据
    net_sent = float(net.bytes_sent / 1024 / 1024)
    # print(f"网络收取{round(net_recv, 2)}M的数据，发送{round(net_sent, 2)}M的数据")

    if len(network_rec) > 10:
        del network_rec[0]
    network_rec.append(round(net_recv, 2))

    if len(network_send) > 10:
        del network_send[0]
    network_send.append(round(net_sent, 2))

    # 获取当前系统时间
    current_time = datetime.datetime.now().strftime("%F %T")  # %F年月日 %T时分秒
    print(f"当前时间是：{current_time}")
    if len(time_list) > 10:
        del time_list[0]
    time_list.append(current_time)
    plt.pause(1)


while True:
    func1()
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    x = range(len(time_list))

    plt.plot(x, cpu_list, marker='o', mec='r', mfc='w', label=u'CPU使用率')
    plt.plot(x, memory_list, marker='*', ms=10, mec='r', mfc='r', label=u'内存使用率')
    plt.plot(x, root_list, marker='1', ms=15, label=u'硬盘使用率')
    plt.plot(x, network_rec, marker='1', ms=15, label=u'网络接收M')
    plt.plot(x, network_send, marker='1', ms=15, label=u'网络发送M')
    plt.legend()  # 让图例生效
    plt.xticks(x, time_list, rotation=105)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(u"time(s)邻居")  # X轴标签
    plt.ylabel("RMSE")  # Y轴标签
    plt.title("网络监控")  # 标题
    plt.show()
