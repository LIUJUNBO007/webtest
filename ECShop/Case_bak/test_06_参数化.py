'''
    3.1 ddt的使用
        1.在测试类前面使用@ddt.ddt
        在测试用例前面使用@ddt.data(测试数据)
        在测试用例前面使用@ddt.unpack--->当测试数据类型为列表嵌套列表时

'''

import unittest
import ddt

test_data = [['诸葛亮', '123456'], ['诸葛亮1', '1234567'], ['诸葛亮2', '1234567']]
test_data_1 = [{"username": "诸葛亮1", "password": "123456"},
               {"username": "诸葛亮2", "password": "123456"},
               {"username": "诸葛亮3", "password": "123456"}]


# 1.创建测试用例
@ddt.ddt()
class TestLogin(unittest.TestCase):
    @ddt.data(*test_data)
    @ddt.unpack  # 获取每组数据的所有值
    def test_login(self, username, password):
        print(f"输入用户名{username}")
        print(f"输入密码{password}")

    @ddt.data(*test_data_1)
    def test_login_1(self, user: dict):
        print(f"输入用户名{user['username']}")
        print(f"输入密码{user['password']}")


if __name__ == '__main__':
    unittest.main()
