import unittest


class TestOder(unittest.TestCase):

    def test_order_info(self):
        print('查看订单详情')
        expected_pay = 100 * 0.9  # 预期结果
        result_pay = 90
        self.assertEqual(expected_pay, result_pay, '实际支付金额和显示金额不一致')

    def test_order_list(self):
        print('查看订单列表')
        order_num = 3
        self.assertTrue(order_num == 3)


if __name__ == '__main__':
    unittest.main()
