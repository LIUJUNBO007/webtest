import unittest


class TestLogin(unittest.TestCase):
    # 创建测试方法(测试用例)
    def test_login(self):
        """登录实例"""
        print('执行登录测试用例')

    def test_get_cart_list(self):
        """查看购物车列表"""
        print('查看购物车列表')

    # 4.添加setup和tearDown
    def setUp(self) -> None:
        print('setUp,在测试用例执行之前,先执行,执行次数和用例条数一致')

    def tearDown(self) -> None:
        print('tearDown,在测试用例执行之后,再执行,执行次数和用例条数一致')

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpclass,在测试类执行之前,先执行,再执行一次')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass,在测试类执行完成之后,再执行,只执行一次')


if __name__ == '__main__':
    unittest.main()
