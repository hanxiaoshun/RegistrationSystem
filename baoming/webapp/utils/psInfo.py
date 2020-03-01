import psutil

virtual_memory = psutil.virtual_memory()
swap_memory = psutil.swap_memory()
print(virtual_memory.total)

g_unit = 1024 * 1024 * 1024


# sswap(total=1073741824, used=150732800, free=923009024, percent=14.0, sin=10705981440, sout=40353792)

class PsInfo(object):
    """
    内存和空间信息
    """

    def __init__(self):
        self.memory_total = round(virtual_memory.total / g_unit)  # 总内存
        self.memory_available = round(virtual_memory.available / g_unit)  # 可用空间
        self.memory_percent = virtual_memory.percent  # 已使用百分比
        self.memory_percent_unused = 100 - virtual_memory.percent  # 未使用百分比
        self.memory_used = round(virtual_memory.used / g_unit)  # 已使用
        self.memory_free = round(virtual_memory.free / g_unit)  # 可用空间
        self.sswap_memory_total = round(swap_memory.total / g_unit)  # 交换区空间
        self.sswap_memory_used = round(swap_memory.used / g_unit)  # 交换区已使用空间
        self.sswap_memory_free = swap_memory.free  # 交换区未可用空间
        self.sswap_memory_percent = swap_memory.free  # 交换区未可用空间
        self.sswap_memory_percent_unused = 100 - swap_memory.free  # 交换区未可用空间


disk_usage = psutil.disk_usage('/')
print(disk_usage)


# sdiskusage(total=998982549504, used=390880133120, free=607840272384, percent=39.1)
class DiskInfo(object):
    """
    磁盘使用信息
    """

    def __init__(self):
        self.disk_total = round(disk_usage.total / g_unit)  #
        self.disk_used = round(disk_usage.used / g_unit)
        self.disk_free = round(disk_usage.free / g_unit)
        self.disk_percent = disk_usage.percent
        self.disk_percent_unused = 100 - disk_usage.percent
