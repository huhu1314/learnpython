# coding=utf-8
# psutil库获取Linux操作系统：内存/cpu/硬盘/登陆用户
import sys
import psutil
import time
import os

time_str = time.strftime("%Y-%m-%d", time.localtime())
file_name = "./" + time_str + ".log"

if os.path.exists(file_name) == False:
    os.mknod(file_name)
    handle = open(file_name, "w")
else:
    handle = open(file_name, "a")

if len(sys.argv) == 1:
    print_type = 1
else:
    print_type = 2


def isset(list_arr, name):
    if name in list_arr:
        return True
    else:
        return False
# cpu利用率
def cpu():
    while True:
        time.sleep(2)
        cpu_liyonglv = psutil.cpu_percent()
        handle.write("当前cpu利用率：%s%%" % cpu_liyonglv)
        print("当前cpu利用率：\033[1;31;42m%s%%\033[0m" % cpu_liyonglv)

print_str = ""
if (print_type == 1) or isset(sys.argv, "mem"):
    memory_convent = 1024 * 1024
    mem = psutil.virtual_memory() # 系统内存
    # 内存使用率 =  (物理内存大小 - 可用内存大小) / 物理内存大小 * 100
    ab = float(mem.used) / float(mem.total) * 100

    handle.write("内存状态如下:\n")
    handle.write("   系统的内存容量为: " + str(mem.total / (memory_convent)) + " MB\n")
    handle.write("   系统的内存已使用容量为: " + str(mem.used / (memory_convent)) + " MB\n")
    handle.write("   系统可用的内存容量为: " + str(mem.total / (memory_convent) - mem.used / (1024 * 1024)) + "MB\n")
    handle.write("   内存的buffer容量为: " + str(mem.buffers / (memory_convent)) + " MB\n")
    handle.write("   内存的cache容量为:" + str(mem.cached / (memory_convent)) + " MB\n")
    handle.write("   内存使用率：%.2f%%" % ab)

    print("内存状态如下:\n")
    print("   系统的内存容量为: " + str(mem.total / (memory_convent)) + " MB\n")
    print("   系统的内存已使用容量为: " + str(mem.used / (memory_convent)) + " MB\n")
    print("   系统可用的内存容量为: " + str(mem.total / (memory_convent) - mem.used / (1024 * 1024)) + "MB\n")
    print("   内存的buffer容量为: " + str(mem.buffers / (memory_convent)) + " MB\n")
    print("   内存的cache容量为:" + str(mem.cached / (memory_convent)) + " MB\n")
    print("   内存使用率：%.2f%%\n" % ab)

if (print_type == 1) or isset(sys.argv, "cpu"):
    cpu_status = psutil.cpu_times()

    handle.write("CPU状态如下:\n")
    handle.write("   user = " + str(cpu_status.user) + "\n")
    handle.write("   nice = " + str(cpu_status.nice) + "\n")
    handle.write("   system = " + str(cpu_status.system) + "\n")
    handle.write("   idle = " + str(cpu_status.idle) + "\n")
    handle.write("   iowait = " + str(cpu_status.iowait) + "\n")
    handle.write("   irq = " + str(cpu_status.irq) + "\n")
    handle.write("   softirq = " + str(cpu_status.softirq) + "\n")
    handle.write("   steal = " + str(cpu_status.steal) + "\n")
    handle.write("   guest = " + str(cpu_status.guest) + "\n")

    print("CPU状态如下:\n")
    print("   user = " + str(cpu_status.user) + "\n")
    print("   nice = " + str(cpu_status.nice) + "\n")
    print("   system = " + str(cpu_status.system) + "\n")
    print("   idle = " + str(cpu_status.idle) + "\n")
    print("   iowait = " + str(cpu_status.iowait) + "\n")
    print("   irq = " + str(cpu_status.irq) + "\n")
    print("   softirq = " + str(cpu_status.softirq) + "\n")
    print("   steal = " + str(cpu_status.steal) + "\n")
    print("   guest = " + str(cpu_status.guest) + "\n")


if (print_type == 1) or isset(sys.argv, "disk"):
    handle.write("磁盘使用率信息如下:\n")
    print("磁盘使用率信息如下:\n")
    # 磁盘使用率
    disk = psutil.disk_partitions()
    for i in disk:
        handle.write("   磁盘：%s   分区格式:%s\n" % (i.device, i.fstype))
        print("   磁盘：%s   分区格式:%s\n" % (i.device, i.fstype))

        disk_use = psutil.disk_usage(i.device)

        handle.write("   使用了：%sM,空闲：%sM,总共：%sM,使用率%s%%\n" % (
        disk_use.used / 1024 / 1024, disk_use.free / 1024 / 1024, disk_use.total / 1024 / 1024, disk_use.percent))
        # \033背景颜色
        print("   使用了：%sM,空闲：%sM,总共：%sM,使用率%s%%\n" % (
            disk_use.used / 1024 / 1024, disk_use.free / 1024 / 1024, disk_use.total / 1024 / 1024, disk_use.percent))


handle.write("---------------------------------------------------------------\n")

# cpu()
handle.close()