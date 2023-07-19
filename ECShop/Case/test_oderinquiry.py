import time
import unittest

import ddt

from Page.BackStageLoginPage import BackStageLoginPage, login_url
from Common.Base import open_browser
from Common.OperationData import OperationData

oderinquiry_data = OperationData('login_data.csv').get_values_to_list()


@ddt.ddt
class TestOder(unittest.TestCase):
    def setUp(self) -> None:
        # 1.打开浏览器
        self.order = BackStageLoginPage(open_browser())
        # 2.进入登录页面
        self.order.open_url(login_url)
        self.order.remove_alerta_window(id='CMask')
        self.order.remove_alerta_window(id='panelCloud')
        # 0.点击ecshop登录按钮
        self.order.click_ecshop()
        time.sleep(2)
        # 1.输入用户名
        username = 'it'
        self.order.input_username(username)
        # 2.输入密码
        password = 'it123456'
        self.order.input_password(password)
        # 4.点击立即登录
        self.order.click_submit()
        time.sleep(5)
        # 5.关闭浏览器
        self.order.close_browser()

        result = self.order.is_register_success(username)  # 实际结果
        self.assertEqual(expected, result)  # 预期结果与实际结果比较
    def tearDown(self) -> None:
        # 7.关闭浏览器
        self.order.close_browser()


if __name__ == '__main__':
    unittest.main()