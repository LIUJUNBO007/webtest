import unittest

platform_name = 1


class TestShopping(unittest.TestCase):
    # 1.登录
    def test_01_login(self):
        print('1.用户的登录')

    # 2.搜索商品
    @unittest.skip(reason="秒杀活动，无须搜索")
    def test_02_search_product(self):
        print('2.搜索商品')

    @unittest.skipIf(platform_name == 1, reason="秒杀活动")
    # 3.添加购物车
    def test_03_add_cart(self):
        print('3.添加购物车')

    @unittest.skipUnless(platform_name == 0, reason="秒杀活动")
    def test_04_add_address(self):
        print('添加收货地址')


if __name__ == '__main__':
    unittest.main()
