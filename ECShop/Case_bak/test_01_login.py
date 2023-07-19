import unittest

class TestLogin(unittest.TestCase):
    # 创建测试方法(测试用例)
    def test_login(self):
        """登录实例"""
        print('执行登录测试用例')

    def test_login_remember_password(self):
        """记住密码登录"""
        print('执行登录用例,记住密码')


if __name__ == '__main__':
    unittest.main()