from django.contrib.auth.hashers import make_password, check_password
import os

os.environ.update({"DJANGO_SETTINGS_MODULE": "baoming.settings"})
from django.test import TestCase


class Password(object):
    """
    密码加密相关
    """

    @staticmethod
    def encryption(password):
        """
        加密
        :param password:
        :return:
        """
        return make_password(password, salt='zdy', hasher='pbkdf2_sha256')

    @staticmethod
    def decrypt_check(password, encryption_password):
        """
        解密
        :param password:
        :return:
        """
        return check_password(password, encryption_password)


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
        print('saddddddddddd')
        pwd = Password()
