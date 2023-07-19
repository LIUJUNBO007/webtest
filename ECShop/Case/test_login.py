import unittest

import ddt

from Page.LoginPage import LoginPage, login_url
from Common.Base import open_browser

login_data = [['诸葛亮', '123456', True],
              ['诸葛', '123456', False],
              ['诸葛亮', '', False]]


@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        # 1.打开浏览器
        self.login = LoginPage(open_browser())
        # 2.进入登录页面
        self.login.open_url(login_url)

    @ddt.data(*login_data)
    @ddt.unpack
    def test_login(self, username, password, expected):
        """测试登录"""
        # 3.输入用户名
        self.login.input_username(username)
        # 4.输入密码
        self.login.input_password(password)
        # 5.点击登录
        self.login.click_submit()
        # 6.断言
        # expected = True #预期结果
        result = self.login.is_login_success(username)  # 实际结果
        self.assertEqual(expected, result)  # 预期结果与实际结果比较

    def tearDown(self) -> None:
        # 7.关闭浏览器
        self.login.close_browser()


if __name__ == '__main__':
    unittest.main()
