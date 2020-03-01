import platform


class SystemInfo(object):
    """
    服务器信息参数
    """

    def __init__(self):
        self.os_name = platform.system()
        self.os_platform = platform.platform()  # 操作系统平台
        self.os_version = platform.version()  # 操作系统版本
        self.os_architecture = platform.architecture()  # 架构，位数
        self.os_machine = platform.machine()  # 计算机类型
        self.os_network_name = platform.node()  # 网络节点名称
        self.os_processor = platform.processor()  # 处理器名称
        self.os_infos = platform.uname()  # 设备信息汇总

    @staticmethod
    def get_platform():
        """获取操作系统名称及版本号"""
        return platform.platform()

    @staticmethod
    def get_version():
        """获取操作系统版本号"""
        return platform.version()

    @staticmethod
    def get_architecture():
        """获取操作系统的位数"""
        return platform.architecture()

    @staticmethod
    def get_machine():
        """计算机类型"""
        return platform.machine()

    @staticmethod
    def get_node():
        """计算机的网络名称"""
        return platform.node()

    @staticmethod
    def get_processor():
        """计算机处理器信息"""
        return platform.processor()

    @staticmethod
    def get_system():
        """获取操作系统类型"""
        return platform.system()

    @staticmethod
    def get_uname():
        """汇总信息"""
        return platform.uname()


class SystemPythonInfo(object):
    """
    获取服务器内部python的信息
    """

    def __init__(self):
        self.python_build = platform.python_build()
        self.python_compiler = platform.python_compiler()
        self.python_branch = platform.python_branch()
        self.python_implementation = platform.python_implementation()
        self.python_revision = platform.python_revision()
        self.python_version_tuple = platform.python_version_tuple()

    @staticmethod
    def get_python_build():
        """ the Python build number and date as strings"""
        return platform.python_build()

    @staticmethod
    def get_python_compiler():
        """Returns a string identifying the compiler used for compiling Python"""
        return platform.python_compiler()

    @staticmethod
    def get_python_branch():
        """Returns a string identifying the Python implementation SCM branch"""
        return platform.python_branch()

    @staticmethod
    def get_python_implementation():
        """Returns a string identifying the Python implementation. Possible return values are: ‘CPython’, ‘IronPython’, ‘Jython’, ‘PyPy’."""
        return platform.python_implementation()

    @staticmethod
    def get_python_version():
        """Returns the Python version as string 'major.minor.patchlevel'
        """
        return platform.python_version()

    @staticmethod
    def get_python_revision():
        """Returns a string identifying the Python implementation SCM revision."""
        return platform.python_revision()

    @staticmethod
    def get_python_version_tuple():
        """Returns the Python version as tuple (major, minor, patchlevel) of strings"""
        return platform.python_version_tuple()


# if __name__ == '__main__':
#     system_info = SystemInfo()
#     python_info = SystemPythonInfo()
#     print(system_info.__dir__()[0:9])
#     print(system_info.__dict__)
#     print("--------------------")
#     print(python_info.__dir__()[1:9])
#     print(python_info.__dict__)
