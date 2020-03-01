from django.contrib.auth.hashers import make_password, check_password
import os

os.environ.update({"DJANGO_SETTINGS_MODULE": "baoming.settings"})
from django.test import TestCase
from webapp.models import *


class File2DB(object):
    """
    密码加密相关
    """

    @staticmethod
    def read():
        """
        读文件
        :param
        :return:
        """
        with open('nation.txt', 'r', encoding='UTF-8') as file:
            for line in file.readlines():
                nation_name = line.split(' ')[1]
                nation = NationInfo()
                nation.nation_name = nation_name
                nation.explain = line
                nation.save()


class PwdTestCase(TestCase):
    def setUp(self):
        pass

    def test_animals_can_speak(self):
        pass

    def test_add_business(self):
        pass

    def test_encryption(self):
        """
        测试密码加密
        """
        File2DB.read()
