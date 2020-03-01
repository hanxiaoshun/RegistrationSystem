import unittest
from django.contrib.auth.hashers import make_password, check_password
import os
from webapp.utils.password import *

os.environ.update({"DJANGO_SETTINGS_MODULE": "baoming.settings"})


class TestDict(unittest.TestCase):
    """
    测试类
    """

    def test_init(self):
        pass

    def test_key(self):
        print(Password.decrypt_check('xzq123456', Password.encryption("xzq123456")))
