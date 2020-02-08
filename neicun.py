# -*- coding: utf-8 -*-
import psutil,time
# 1.监控服务器cpu使用率
def cpu():
    while True:
        time.sleep(1)
        cpu_liyonglv = psutil.cpu_percent()
        print("当前cpu利用率：\033[1;31;42m%s%%\033[0m" % cpu_liyonglv)
cpu()

def neicun():
    while True:
        time.sleep(1)
        cpu_liyonglv = psutil.cpu_percent()
        print("当前内存利用率：\033[1;31;42m%s%%\033[0m" % cpu_liyonglv)