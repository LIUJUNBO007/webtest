import time
import unittest

import ddt

from Page.RegisterPage import RegisterPage, regiser_url
from Common.Base import open_browser

login_data = [['诸葛亮100', '1212234256@163.com', '123456', '123456', '11111111', '123456789', '1234564', '55555555', '123456',
               5, True],
              ['诸葛亮100', '112324536@163.com', '123456', '123456', '11111111', '123456789', '1234564', '55555555', '123456',
               5, False],
              ]


@ddt.ddt
class TestRegister(unittest.TestCase):
    def setUp(self) -> None:
        # 1.打开浏览器
        self.register = RegisterPage(open_browser())
        # 2.进入登录页面
        self.register.open_url(regiser_url)

    @ddt.data(*login_data)
    @ddt.unpack
    # username, password,comformpassword,qq,officephone,homephone,mobilephone,passwdanswer
    def test_login(self, username, email, password, comformpassword, qq, officephone, homephone, mobilephone,
                   passwdanswer, index, expected):
        """测试登录"""
        # 3.输入用户名
        self.register.input_username(username)
        self.register.input_email(email)
        # 4.输入密码
        self.register.input_password(password)
        self.register.input_conform_password(comformpassword)
        self.register.input_qq(qq)
        self.register.input_office_phone(officephone)
        self.register.input_home_phone(homephone)
        self.register.input_mobilephone(mobilephone)
        self.register.input_passwd_answer(passwdanswer)
        self.register.search_passwd_question(index)
        # 5.点击登录
        self.register.click_submit()

        # 6.断言
        result = self.register.is_register_success(username)  # 实际结果
        self.assertEqual(expected, result)  # 预期结果与实际结果比较

    def tearDown(self) -> None:
        # 7.关闭浏览器
        self.register.close_browser()


if __name__ == '__main__':
    unittest.main()
