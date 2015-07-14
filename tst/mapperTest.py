import unittest
from definitions import *

class MapperTest(unittest.TestCase):
    def test_attr_and_wrap_keyword(self):
        UserMapper.prepare()
        user_model = UserModel()

        user = user_model.to_vo()

        self.assertEquals('Melody, a@b.cn, mm', str(user))
        self.assertEquals("<class 'definitions.user.User'>", str(type(user)))
        self.assertEquals("<type 'str'>", str(type(user.nickname)))
        self.assertEquals("<class 'definitions.user.Contact'>", str(type(user.contact)))
